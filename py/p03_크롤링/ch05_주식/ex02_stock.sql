-- SQL 주석
# MySQL 주석
-- 데이터베이스 생성
CREATE SCHEMA `stock`;

-- 데이터베이스 선택
USE stock;

-- 테이블 생성
-- INT(4byte) -> ±21억
-- FLOAT(4byte) 
-- 양수범위: 1.157x10-38 ~ 3.402x10+38
-- 음수범위: -3.402x10-38 ~ -1.175x10+38
-- BIGINT(8byte) -> ±922경
-- VARCHAR(100) -> 100byte
CREATE TABLE `stock`.`daily_market` (
  `seq` INT NOT NULL AUTO_INCREMENT,
  `dt` DATE NULL,
  `item_name` VARCHAR(100) NULL,
  `item_code` VARCHAR(100) NULL,
  `price` BIGINT NULL,
  `foreign_ownership_ratio` FLOAT NULL,
  `rel_return` FLOAT NULL,
  `per` FLOAT NULL,
  `per_12m` FLOAT NULL,
  `per_ind` FLOAT NULL,
  `pbr` FLOAT NULL,
  `dividend_yield` FLOAT NULL,
  `volume` BIGINT NULL,
  `trans_price` BIGINT NULL,
  `market_capital_prefer` BIGINT NULL,
  `market_capital_common` BIGINT NULL,
  PRIMARY KEY (`seq`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COMMENT = '주식 마켓';

-- 조회(Read)
SELECT * FROM stock.daily_market;