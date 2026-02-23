import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class ThePublisher(Node):

    def __init__(self):
        super().__init__('N1_agb')
        self.publisher_ = self.create_publisher(Int32, 'numbers_agb', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

        self.primes = self.prime_numbers(100)
        self.index = 0

    def timer_callback(self):
        if self.index >= len(self.primes):
            self.get_logger().warning('No more prime numbers')
            return

        msg = Int32()
        msg.data = self.primes[self.index]
        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: {msg.data}')
        self.index += 1

    def prime_numbers(self, n):
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for divisor in range(2, int(num**0.5) + 1):
                if num % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes


def main(args=None):
    rclpy.init(args=args)
    node = ThePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
