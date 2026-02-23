import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class DistanceGenerator(Node):

    def __init__(self):
        super().__init__('distance_generator')

        self.publisher_ = self.create_publisher(
            Float32,
            '/agb/distance_raw',
            10
        )

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(0.3, 10.0)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Generated distance: {msg.data:.2f} m')


def main(args=None):
    rclpy.init(args=args)
    node = DistanceGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()