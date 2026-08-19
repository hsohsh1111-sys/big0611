-- SQL 주석
# MYSQL 주석alter
CREATE SCHEMA `stock` ;


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
COLLATE = utf8mb4_0900_ai_ci
COMMENT = '주식마켓';


-- 조회 (Read)
SELECT * FROM stock.daily_market;