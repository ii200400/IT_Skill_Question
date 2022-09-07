#!/usr/bin/env python
# -*- coding: utf-8 -*-

# S자 형태로 주행하는 자동차 스크립트

# 1번째 줄은 환경 변수에서 지정한 언어의 위치를 찾아 실행하는 명령어
# 2번째 줄은 필자가 한글을 작성하기 위해 인코딩 설정을 utf-8로 설정하는 명령어
# 두 줄은 #으로 시작하지만 주석처리된 것이 아니다. 게다가 최상단에 작성해주어야 한다.

# 노드를 python으로 작성하기 위한 필수 라이브러리
# rospy를 통해 ros topics, service, parameters를 python을 통해 접근 가능하도록 한다.
import rospy
# 시뮬레이터 메시지를 가져올 수 있도록 morai_msg의 CtrlCmd를 사용한다.
# 시뮬레이터에서 본 morai_msg/CtrlCmd 을 의미한다.
from morai_msgs.msg import CtrlCmd

class s_drive():
    # 클래스 생성 시 바로 불리는 함수로 기억한다, 이름 그대로 초기화를 하는 경우가 많았다.
    def __init__(self):
        # 프로세스와 통신 초기화
        # rospy에서는 꼭 노드의 고유 이름을 알아야 통신이 가능한데 여기에서는 s_drive라고 해준다.
        rospy.init_node('s_drive', anonymous=True)

        # 시뮬레이터로 메시지를 publish 하기 위해 publish 클래스 생성
        # 매개변수는 순서대로 (토픽명, 메시지 클래스, 큐의 크기)
        # 시뮬레이터의 F4를 누르면 나오는 cmd Control 탭의 
        # Message Type(morai_msgs/CtrlCmd)과 Message Topic(/ctrl_cmd)에 들어간다.
        cmd_pub = rospy.Publisher('ctrl_cmd', CtrlCmd, queue_size=1)

        # 주기 설정, 아래는 30Hz로 반복한다는 내용
        rate = rospy.Rate(30)

        # CtrlCmd 클래스 생성 및 값 설정
        # 후에 CtrlCmd는 시뮬레이터로 보내는 메시지로 발송된다.
        cmd = CtrlCmd()
        cmd.longlCmdType = 2
        cmd.velocity = 10

        # 좌우로(S자로) 움직이는 자동차를 위해서 조항각 변수를 배열로 넣어 조작할 예정
        # 아래의 코드에서 cmd에 설정해준다.
        # 참고로 0 일 때는 우회전, 1 일때는 좌회전이다.
        steering_cmd = [-0.2, 0.2]
        # 토픽 전송 수
        cmd_cnts = 50

        # rospy가 shoutdown 될 때까지 반복
        while not rospy.is_shutdown():
            for i in range(2):
                # 위에서 만든 배열이 번갈아 들어가게 된다
                cmd.steering = steering_cmd[i]

                # 
                rospy.loginfo(cmd)

                # 우로 50회 좌로 50회 작동하게 된다.
                for _ in range(cmd_cnts):
                    # 시뮬레이션으로 publish 한다.
                    cmd_pub.publish(cmd)
                    # rate에서 설정한 시간만큼 대기
                    rate.sleep()

# 파이썬 실행문
if __name__ == '__main__':
    try:
        # s_drive 클래스 생성 및 변수에 저장
        s_d = s_drive()
    except rospy.ROSInterruptException:
        pass
