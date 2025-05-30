-- MySQL Script generated by MySQL Workbench
-- Wed Sep 14 20:07:47 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineerin

-- Schema Mecânica Oficina
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Mecânica Oficina` DEFAULT CHARACTER SET utf8 ;
USE `Mecânica Oficina` ;

-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NULL,
  `CPF` VARCHAR(45) NULL,
  `Telefone` INT NULL,
  `Endereço` VARCHAR(45) NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Equipe de mecânicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Equipe de mecânicos` (
  `idEquipe de mecânicos` INT NOT NULL,
  `idVeículo` INT NOT NULL,
  PRIMARY KEY (`idEquipe de mecânicos`),
  CONSTRAINT `fk_Equipe de mecânicos_Veículo1`
    FOREIGN KEY (`idVeículo`)
    REFERENCES `Mecânica Oficina`.`Veículo` (`idVeículo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Equipe de mecânicos_Veículo1_idx` ON `Mecânica Oficina`.`Equipe de mecânicos` (`idVeículo` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Mecânicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Mecânicos` (
  `idMecânicos` INT NOT NULL,
  `Matricula` INT NULL,
  `Nome` VARCHAR(45) NULL,
  `Endereço` VARCHAR(45) NULL,
  `Especialidade` VARCHAR(45) NULL,
  PRIMARY KEY (`idMecânicos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`OS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`OS` (
  `idOS` INT NOT NULL,
  `Cod` VARCHAR(45) NULL,
  `Data emissão` DATE NULL,
  `Valor` FLOAT NULL,
  `Data entrega` VARCHAR(45) NULL,
  `Status_idStatus` INT NOT NULL,
  `OS-Serviço_idOS-Serviço` INT NOT NULL,
  `OS-Produto_idOS-Produto` INT NOT NULL,
  PRIMARY KEY (`idOS`),
  CONSTRAINT `fk_OS_Status1`
    FOREIGN KEY (`Status_idStatus`)
    REFERENCES `Mecânica Oficina`.`Status` (`idStatus`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_OS_OS-Serviço1`
    FOREIGN KEY (`OS-Serviço_idOS-Serviço`)
    REFERENCES `Mecânica Oficina`.`OS-Serviço` (`idOS-Serviço`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_OS_OS-Produto1`
    FOREIGN KEY (`OS-Produto_idOS-Produto`)
    REFERENCES `Mecânica Oficina`.`OS-Produto` (`idOS-Produto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_OS_Status1_idx` ON `Mecânica Oficina`.`OS` (`Status_idStatus` ASC) VISIBLE;

CREATE INDEX `fk_OS_OS-Serviço1_idx` ON `Mecânica Oficina`.`OS` (`OS-Serviço_idOS-Serviço` ASC) VISIBLE;

CREATE INDEX `fk_OS_OS-Produto1_idx` ON `Mecânica Oficina`.`OS` (`OS-Produto_idOS-Produto` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`OS-Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`OS-Produto` (
  `idOS-Produto` INT NOT NULL,
  `Valor` FLOAT NULL,
  `Quantidade` VARCHAR(45) NULL,
  `Produto_idProduto` INT NOT NULL,
  PRIMARY KEY (`idOS-Produto`),
  CONSTRAINT `fk_OS-Produto_Produto1`
    FOREIGN KEY (`Produto_idProduto`)
    REFERENCES `Mecânica Oficina`.`Produto` (`idProduto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_OS-Produto_Produto1_idx` ON `Mecânica Oficina`.`OS-Produto` (`Produto_idProduto` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`OS-Serviço`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`OS-Serviço` (
  `idOS-Serviço` INT NOT NULL,
  `Valor` FLOAT NULL,
  `idTipo de Serviço` INT NOT NULL,
  PRIMARY KEY (`idOS-Serviço`),
  CONSTRAINT `fk_OS-Serviço_Tipo de Serviço1`
    FOREIGN KEY (`idTipo de Serviço`)
    REFERENCES `Mecânica Oficina`.`Tipo de Serviço` (`idTipo de Serviço`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_OS-Serviço_Tipo de Serviço1_idx` ON `Mecânica Oficina`.`OS-Serviço` (`idTipo de Serviço` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Produto` (
  `idProduto` INT NOT NULL,
  `Valor` FLOAT NULL,
  `Descrição` VARCHAR(45) NULL,
  `Estoque` VARCHAR(45) NULL,
  PRIMARY KEY (`idProduto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Serviço`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Serviço` (
  `idServiço` INT NOT NULL,
  `Equipe de mecânicos_idEquipe de mecânicos` INT NOT NULL,
  `idMecânicos` INT NOT NULL,
  `OS_idOS` INT NOT NULL,
  PRIMARY KEY (`idServiço`),
  CONSTRAINT `fk_Serviço_Equipe de mecânicos1`
    FOREIGN KEY (`Equipe de mecânicos_idEquipe de mecânicos`)
    REFERENCES `Mecânica Oficina`.`Equipe de mecânicos` (`idEquipe de mecânicos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Serviço_Mecânicos1`
    FOREIGN KEY (`idMecânicos`)
    REFERENCES `Mecânica Oficina`.`Mecânicos` (`idMecânicos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Serviço_OS1`
    FOREIGN KEY (`OS_idOS`)
    REFERENCES `Mecânica Oficina`.`OS` (`idOS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Serviço_Equipe de mecânicos1_idx` ON `Mecânica Oficina`.`Serviço` (`Equipe de mecânicos_idEquipe de mecânicos` ASC) VISIBLE;

CREATE INDEX `fk_Serviço_Mecânicos1_idx` ON `Mecânica Oficina`.`Serviço` (`idMecânicos` ASC) VISIBLE;

CREATE INDEX `fk_Serviço_OS1_idx` ON `Mecânica Oficina`.`Serviço` (`OS_idOS` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Status` (
  `idStatus` INT NOT NULL,
  `Descrição` VARCHAR(45) NULL,
  PRIMARY KEY (`idStatus`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Tabela de valores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Tabela de valores` (
  `idTabela_de_valores` INT NOT NULL,
  `Valor de revisao Periodica` FLOAT NULL,
  `Valor manutenção` FLOAT NULL,
  `Valor m-d-o` FLOAT NULL,
  `OS-Serviço_idOS-Serviço` INT NOT NULL,
  `OS-Produto_idOS-Produto` INT NOT NULL,
  PRIMARY KEY (`idTabela_de_valores`),
  CONSTRAINT `fk_Tabela de valores_OS-Serviço1`
    FOREIGN KEY (`OS-Serviço_idOS-Serviço`)
    REFERENCES `Mecânica Oficina`.`OS-Serviço` (`idOS-Serviço`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tabela de valores_OS-Produto1`
    FOREIGN KEY (`OS-Produto_idOS-Produto`)
    REFERENCES `Mecânica Oficina`.`OS-Produto` (`idOS-Produto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Tabela de valores_OS-Serviço1_idx` ON `Mecânica Oficina`.`Tabela de valores` (`OS-Serviço_idOS-Serviço` ASC) VISIBLE;

CREATE INDEX `fk_Tabela de valores_OS-Produto1_idx` ON `Mecânica Oficina`.`Tabela de valores` (`OS-Produto_idOS-Produto` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Tipo de Serviço`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Tipo de Serviço` (
  `idTipo de Serviço` INT NOT NULL,
  `Valores` FLOAT NULL,
  PRIMARY KEY (`idTipo de Serviço`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mecânica Oficina`.`Veículo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Mecânica Oficina`.`Veículo` (
  `idVeículo` INT NOT NULL,
  `Placa` VARCHAR(45) NULL,
  `Marcar` VARCHAR(45) NULL,
  `Cor` VARCHAR(45) NULL,
  `Ano` DATE NULL,
  `Cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idVeículo`),
  CONSTRAINT `fk_Veículo_Cliente1`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `Mecânica Oficina`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Veículo_Cliente1_idx` ON `Mecânica Oficina`.`Veículo` (`Cliente_idCliente` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;