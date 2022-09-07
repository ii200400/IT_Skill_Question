#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from morai_msgs.msg import CtrlCmd, CollisionData, EgoVehicleStatus, EventInfo
from morai_msgs.srv import MoraiEventCmdSrv
from enum import Enum

# 차량의 기어, String을 받아오면 숫자로 변환한다.
class Gear(Enum):
    P = 1
    R = 2
    N = 3
    D = 4

class s_drive():
    def __init__(self):
        # 노드 정의
        rospy.init_node('collision_avoid', anonymous=True)
        
        # publisher 정의 
        # 시뮬레이터로 조향 데이터를 보내기 위함
        self.cmd_pub = rospy.Publisher('/ctrl_cmd', CtrlCmd, queue_size=1)
        
        # subscriber 정의
        # 시뮬레이터로부터 충돌과 차량의 상태 데이터를 받기 위함
        rospy.Subscriber('/CollisionData', CollisionData, self.collision_callback)
        rospy.Subscriber('/Ego_topic', EgoVehicleStatus, self.ego_callback)

        # service 정의
        # 시뮬레이터로 특정 이벤트마다 기어를 변경해주기 위함
        rospy.wait_for_service('/Service_MoraiEventCmd')
        self.event_cmd_srv = rospy.ServiceProxy('Service_MoraiEventCmd', MoraiEventCmdSrv)

        # rate는 10hz(0.1초)로 설정
        self.rate = rospy.Rate(10)

        self.is_collision = False
        self.ego_status = EgoVehicleStatus()

        # 처음에 auto_mode , drive gear로 세팅
        # 시뮬레이터에서 'q'를 누르지 않아도 자동으로 auto모드가 된다고.. 한다.
        self.send_gear_cmd(Gear.D.value)

        while not rospy.is_shutdown():
            # 충돌 발생 확인
            if(self.is_collision):
                # 충돌이 발생하면 후진기어로 변경
                self.send_gear_cmd(Gear.R.value)
                
                # 2초간 0.4rad로 조항, 10kph의 속도로 진행
                for _ in range(20):
                    self.send_ctrl_cmd(0.4, 10)
                    self.rate.sleep()
                
                # 직진기어로 변경
                self.send_gear_cmd(Gear.D.value)

            else:
                # 충돌하지 않았다면 10kph의 속도로 직진
                self.send_ctrl_cmd(0, 10)
                self.rate.sleep()

    # 충돌 메시지 콜백 함수
    def collision_callback(self, data):
        # 충돌을 했다면 아래의 변수가 True, 
        # 그렇지 않다면 False로 바꿔 충돌 확인이 되도록 한다.
        if(len(data.collision_object) > 0):
            self.is_collision = True
        else:
            self.is_collision = False

    # EGO 차량 상태 정보 콜백 함수
    def ego_callback(self, data):
        print(self.ego_status.velocity.x)
        self.ego_status = data

    # 기어 변경 이벤트 메시지 세팅 함수
    def send_gear_cmd(self, gear_mode):
        # 기어 변경이 제대로 되기 위해서는 차량 속도가 약 0 이어야함
        while( abs(self.ego_status.velocity.x) > 0.1):
            self.send_ctrl_cmd(0,0)
            self.rate.sleep()
        
        gear_cmd = EventInfo()
        gear_cmd.option = 3
        gear_cmd.ctrl_mode = 3
        gear_cmd.gear = gear_mode
        gear_cmd_resp = self.event_cmd_srv(gear_cmd)
        rospy.loginfo(gear_cmd)

    # ctrl_cmd 메시지 세팅 함수
    def send_ctrl_cmd(self, steering ,velocity):
        cmd = CtrlCmd()
        if(velocity > 0):
            cmd.longlCmdType = 2
            cmd.velocity = velocity
            cmd.steering = steering
        else:
            cmd.longlCmdType = 1
            cmd.brake = 1
            cmd.steering = 0
        self.cmd_pub.publish(cmd)


if __name__ == '__main__':
    try:
        s_d = s_drive()
    except rospy.ROSInterruptException:
        pass
