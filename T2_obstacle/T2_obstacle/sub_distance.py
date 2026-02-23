import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistanceMonitor(Node):

    def __init__(self):
        super().__init__('distance_monitor')

        self.subscription = self.create_subscription(
            Float32,
            '/agb/ultrasonic',
            self.listener_callback,
            10
        )

        self.alert_threshold = 5.0  # meters

    def listener_callback(self, msg):
        distance = msg.data

        self.get_logger().info(
            f'Distance received: {distance:.2f} m'
        )

        if distance < self.alert_threshold:
            self.get_logger().warn(
                f'Distance below threshold ({distance:.2f} m < {self.alert_threshold:.2f} m)'
            )


def main(args=None):
    rclpy.init(args=args)
    node = DistanceMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()