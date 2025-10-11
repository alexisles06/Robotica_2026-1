#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from math import sin
from std_msgs.msg import Float64

class MyPublish(Node):
    def __init__(self):
        super().__init__('publish_node')
        self.number_ = 0.0
        self.suma = 0.0
        self.aumento_=0.1
        self.publisher_ =self.create_publisher(Float64, 'publish_topic', 10)
        self.get_logger().info('Nodo publicador activo')
        self.create_timer(0.5,self.subcallback)

    def subcallback(self):
        msg = Float64()
        self.suma += self.aumento_
        msg.data = sin(self.suma)
        self.publisher_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = MyPublish()
    rclpy.spin(node)
    rclpy.shutdown()

    if __name__ == "__main__":
        main()