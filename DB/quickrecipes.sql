-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 04, 2021 at 08:15 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quickrecipes`
--

-- --------------------------------------------------------

--
-- Table structure for table `Access`
--

CREATE TABLE `Access` (
  `id_access` int(10) NOT NULL,
  `id_user` int(10) NOT NULL,
  `date` date NOT NULL,
  `request_type` varchar(255) NOT NULL,
  `request_url` varchar(255) NOT NULL,
  `public_ip` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `AmountType`
--

CREATE TABLE `AmountType` (
  `id_amount_type` int(10) NOT NULL,
  `amount_type_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `AmountType`
--

INSERT INTO `AmountType` (`id_amount_type`, `amount_type_name`) VALUES
(1, 'g'),
(2, 'mg'),
(3, 'piece');

-- --------------------------------------------------------

--
-- Table structure for table `Ingredientes_Receita`
--

CREATE TABLE `Ingredientes_Receita` (
  `id_ingredient` int(10) NOT NULL,
  `id_recipe` int(10) NOT NULL,
  `amount` int(10) NOT NULL,
  `id_amount_type` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Ingredientes_Receita`
--

INSERT INTO `Ingredientes_Receita` (`id_ingredient`, `id_recipe`, `amount`, `id_amount_type`) VALUES
(1, 14, 12, 3),
(1, 19, 1, 3),
(2, 19, 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `Ingredients`
--

CREATE TABLE `Ingredients` (
  `id_ingredient` int(10) NOT NULL,
  `id_user` int(11) NOT NULL,
  `nome_ingredient` varchar(255) NOT NULL,
  `calories` int(10) NOT NULL,
  `created_at` date NOT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Ingredients`
--

INSERT INTO `Ingredients` (`id_ingredient`, `id_user`, `nome_ingredient`, `calories`, `created_at`, `type`) VALUES
(1, 10, 'apple', 100, '2020-12-23', 'fruit'),
(2, 10, 'banana', 56, '2020-12-23', 'fruit'),
(3, 10, 'Tomate', 12, '2021-01-02', 'fruit'),
(4, 10, 'canela', 0, '2021-01-02', 'pó mágico');

-- --------------------------------------------------------

--
-- Table structure for table `Nutrition`
--

CREATE TABLE `Nutrition` (
  `id_nutrition` int(10) NOT NULL,
  `calories` int(10) DEFAULT NULL,
  `carbs` int(10) DEFAULT NULL,
  `fat` int(10) DEFAULT NULL,
  `protein` int(10) DEFAULT NULL,
  `fiber` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Nutrition`
--

INSERT INTO `Nutrition` (`id_nutrition`, `calories`, `carbs`, `fat`, `protein`, `fiber`) VALUES
(1, 54, 20, 12, 3, 0),
(11, 0, 0, 283, 0, 0),
(17, 0, 0, 283, 0, 0),
(18, 0, 0, 283, 0, 0),
(19, 0, 0, 283, 0, 0),
(25, 19, 0, 25, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `Recipe`
--

CREATE TABLE `Recipe` (
  `id_recipe` int(10) NOT NULL,
  `id_nutrition` int(10) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `instructions` varchar(255) NOT NULL,
  `image_link` varchar(255) NOT NULL,
  `image_type` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  `id_user` int(10) DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  `visible` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Recipe`
--

INSERT INTO `Recipe` (`id_recipe`, `id_nutrition`, `title`, `description`, `instructions`, `image_link`, `image_type`, `created_at`, `id_user`, `updated_at`, `visible`) VALUES
(7, 17, 'teste de teste', ' teste de teste de teste', '- cozinhar 300 graus e durante 30min', '-', 'jpg', '2020-12-27', 10, '0000-00-00', 1),
(9, 19, 'teste de teste', ' teste de teste de teste', '- cozinhar 300 graus e durante 30min', '-', 'jpg', '2020-12-27', 10, '0000-00-00', 1),
(14, 17, 'teste de teste', ' teste de teste de teste', '- cozinhar 300 graus e durante 30min', '-', 'jpg', '2020-12-27', 10, '0000-00-00', 0),
(19, 25, 'Ramen', 'muito bom, 99.9% saudavel', 'caldo de carne, molho de soja, peço desculpa ', '-', 'jpg', '2020-12-27', 10, '2020-12-27', 1);

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id_user` int(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  `api_key` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id_user`, `name`, `email`, `created_at`, `api_key`) VALUES
(10, 'daniel', 'teste@teste.pt', '2020-12-22', 'Nr4SRPJg0mZnhw'),
(22, 'duarte', 'duarte@teste.pt', '2020-12-22', '8ImMwlRvvkdN7Q');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Access`
--
ALTER TABLE `Access`
  ADD PRIMARY KEY (`id_access`),
  ADD KEY `FKAccess142946` (`id_user`);

--
-- Indexes for table `AmountType`
--
ALTER TABLE `AmountType`
  ADD PRIMARY KEY (`id_amount_type`);

--
-- Indexes for table `Ingredientes_Receita`
--
ALTER TABLE `Ingredientes_Receita`
  ADD PRIMARY KEY (`id_ingredient`,`id_recipe`),
  ADD KEY `FKIngredient301820` (`id_recipe`),
  ADD KEY `FKIngredient406279` (`id_amount_type`);

--
-- Indexes for table `Ingredients`
--
ALTER TABLE `Ingredients`
  ADD PRIMARY KEY (`id_ingredient`);

--
-- Indexes for table `Nutrition`
--
ALTER TABLE `Nutrition`
  ADD PRIMARY KEY (`id_nutrition`);

--
-- Indexes for table `Recipe`
--
ALTER TABLE `Recipe`
  ADD PRIMARY KEY (`id_recipe`),
  ADD KEY `FKRecipe313651` (`id_nutrition`),
  ADD KEY `FKRecipe689780` (`id_user`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Access`
--
ALTER TABLE `Access`
  MODIFY `id_access` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `AmountType`
--
ALTER TABLE `AmountType`
  MODIFY `id_amount_type` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Ingredients`
--
ALTER TABLE `Ingredients`
  MODIFY `id_ingredient` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Nutrition`
--
ALTER TABLE `Nutrition`
  MODIFY `id_nutrition` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `Recipe`
--
ALTER TABLE `Recipe`
  MODIFY `id_recipe` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id_user` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Access`
--
ALTER TABLE `Access`
  ADD CONSTRAINT `FKAccess142946` FOREIGN KEY (`id_user`) REFERENCES `Users` (`id_user`);

--
-- Constraints for table `Ingredientes_Receita`
--
ALTER TABLE `Ingredientes_Receita`
  ADD CONSTRAINT `FKIngredient301820` FOREIGN KEY (`id_recipe`) REFERENCES `Recipe` (`id_recipe`),
  ADD CONSTRAINT `FKIngredient406279` FOREIGN KEY (`id_amount_type`) REFERENCES `AmountType` (`id_amount_type`),
  ADD CONSTRAINT `FKIngredient441362` FOREIGN KEY (`id_ingredient`) REFERENCES `Ingredients` (`id_ingredient`);

--
-- Constraints for table `Recipe`
--
ALTER TABLE `Recipe`
  ADD CONSTRAINT `FKRecipe313651` FOREIGN KEY (`id_nutrition`) REFERENCES `Nutrition` (`id_nutrition`),
  ADD CONSTRAINT `FKRecipe689780` FOREIGN KEY (`id_user`) REFERENCES `Users` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
