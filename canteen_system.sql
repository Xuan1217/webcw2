/*
Navicat MySQL Data Transfer

Source Server         : XW
Source Server Version : 80016
Source Host           : localhost:3306
Source Database       : canteen_system

Target Server Type    : MYSQL
Target Server Version : 80016
File Encoding         : 65001

Date: 2022-12-27 15:53:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for car
-- ----------------------------
DROP TABLE IF EXISTS `car`;
CREATE TABLE `car` (
  `Aid` int(11) NOT NULL AUTO_INCREMENT,
  `Uid` int(11) DEFAULT NULL,
  `Cid` int(11) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `dish` varchar(100) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `Num` int(11) DEFAULT NULL,
  PRIMARY KEY (`Aid`),
  KEY `Uid` (`Uid`),
  KEY `Cid` (`Cid`),
  CONSTRAINT `car_ibfk_1` FOREIGN KEY (`Uid`) REFERENCES `user` (`Uid`),
  CONSTRAINT `car_ibfk_2` FOREIGN KEY (`Cid`) REFERENCES `dishes` (`Cid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of car
-- ----------------------------
INSERT INTO `car` VALUES ('1', '6', '1', '../static/picture/1.png', 'Durain Pizza', '124', '1');
INSERT INTO `car` VALUES ('2', '3', '1', '../static/picture/1.png', 'Durain Pizza', '124', '1');
INSERT INTO `car` VALUES ('3', '1', '2', '../static/picture/2.png', 'Sirloin Steak', '232', '1');
INSERT INTO `car` VALUES ('4', '1', '1', '../static/picture/1.png', 'Durain Pizza', '124', '1');
INSERT INTO `car` VALUES ('5', '1', '1', '../static/picture/1.png', 'Durain Pizza', '124', '1');

-- ----------------------------
-- Table structure for dishes
-- ----------------------------
DROP TABLE IF EXISTS `dishes`;
CREATE TABLE `dishes` (
  `Cid` int(11) NOT NULL AUTO_INCREMENT,
  `dish` varchar(100) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `inventory` int(11) DEFAULT NULL,
  `likeNum` int(11) DEFAULT NULL,
  PRIMARY KEY (`Cid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dishes
-- ----------------------------
INSERT INTO `dishes` VALUES ('1', 'Durain Pizza', '../static/picture/1.png', '124', '271', '0');
INSERT INTO `dishes` VALUES ('2', 'Sirloin Steak', '../static/picture/2.png', '232', '12', '0');
INSERT INTO `dishes` VALUES ('3', 'shredded pork with garlic sauce', '../static/picture/4.png', '29', '18', '0');
INSERT INTO `dishes` VALUES ('5', 'Caisa Salad', '../static/picture/3.png', '12', '4', '0');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Uid` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(500) DEFAULT NULL,
  `Password` varchar(500) DEFAULT NULL,
  `Currency` int(11) DEFAULT NULL,
  PRIMARY KEY (`Uid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'abcd', '1234', '488');
INSERT INTO `user` VALUES ('3', 'linJ', '123456', '9951');
INSERT INTO `user` VALUES ('6', 'wzc', '1234', '0');
