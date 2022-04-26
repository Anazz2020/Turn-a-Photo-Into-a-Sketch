# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    image.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anazz <lovewithacoco10@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/26 06:13:47 by anazz             #+#    #+#              #
#    Updated: 2022/04/26 06:13:49 by anazz            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import cv2


image=cv2.imread("1.jpg")
grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertblur=cv2.bitwise_not(blur)

sketch=cv2.divide(grey,invertblur,scale=260)
cv2.imwrite("sketch.png",sketch)
