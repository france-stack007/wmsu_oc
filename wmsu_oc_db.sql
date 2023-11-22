-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 10, 2023 at 03:17 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wmsu_oc_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `food_name` varchar(255) NOT NULL,
  `store` varchar(255) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`id`, `customer_id`, `food_name`, `store`, `quantity`, `price`, `total`, `date_created`) VALUES
(81, 6, 'Kari', 'Melriss Store', 1, 40, 40, '2023-11-10 00:04:49'),
(82, 6, 'chicken', 'Melriss Store', 1, 45, 45, '2023-11-10 00:04:53'),
(83, 6, 'Kari', 'Melriss Store', 1, 40, 40, '2023-11-10 00:06:32'),
(84, 6, 'Kari', 'Melriss Store', 1, 40, 40, '2023-11-10 00:06:38'),
(85, 6, 'Kari', 'Melriss Store', 1, 40, 40, '2023-11-10 00:07:27');

-- --------------------------------------------------------

--
-- Table structure for table `complete__delivery`
--

CREATE TABLE `complete__delivery` (
  `id` int(11) NOT NULL,
  `track_no` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `food_name` varchar(255) NOT NULL,
  `vendor` varchar(255) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `mop` varchar(255) NOT NULL,
  `payment` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `response` varchar(255) NOT NULL,
  `food_ready` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `delivery`
--

CREATE TABLE `delivery` (
  `id` int(11) NOT NULL,
  `track_no` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `food_name` varchar(255) NOT NULL,
  `vendor` varchar(255) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `response` varchar(255) NOT NULL,
  `mop` varchar(255) NOT NULL,
  `food_ready` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `delivery`
--

INSERT INTO `delivery` (`id`, `track_no`, `customer_id`, `food_name`, `vendor`, `quantity`, `price`, `total`, `location`, `response`, `mop`, `food_ready`, `date_created`) VALUES
(13, 45989479, 6, 'Kari', 'Melriss Store', 1, 40, 40, '', 'Pending', 'pickup', 'No', '2023-11-09 23:59:55');

-- --------------------------------------------------------

--
-- Table structure for table `fee`
--

CREATE TABLE `fee` (
  `id` int(11) NOT NULL,
  `fees` int(11) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fee`
--

INSERT INTO `fee` (`id`, `fees`, `date_created`) VALUES
(1, 30, '2023-11-07 22:43:12');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `id` int(11) NOT NULL,
  `food_name` varchar(255) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `status` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `vendor_id` int(11) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`id`, `food_name`, `price`, `status`, `category`, `image_url`, `vendor_id`, `date_created`) VALUES
(1, 'Rice', 20, 'Available', 'Solo Meal', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 2, '2023-11-02 21:18:09'),
(2, 'chicken', 45, 'Available', 'Solo Meal', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 2, '2023-11-02 22:51:34'),
(3, 'Rice', 30, 'Not Available', 'Solo Meal', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 1, '2023-11-03 01:25:11'),
(4, 'Adobo', 50, 'Available', 'Solo Meal', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 1, '2023-11-03 01:25:34'),
(5, 'Desirae Marks', 639, 'Available', 'Desserts', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 1, '2023-11-05 15:21:47'),
(6, 'Kari', 40, 'Available', 'Combo Meal', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 2, '2023-11-09 21:12:48');

-- --------------------------------------------------------

--
-- Table structure for table `remittance`
--

CREATE TABLE `remittance` (
  `id` int(11) NOT NULL,
  `track_no` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `mop` varchar(255) NOT NULL,
  `payment` varchar(255) NOT NULL,
  `refereance` int(11) DEFAULT NULL,
  `errand` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `role` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `role`, `date_created`) VALUES
(1, 'customer', '2023-11-02 19:19:35'),
(2, 'admin', '2023-11-02 19:19:35'),
(3, 'vendor', '2023-11-02 20:40:18'),
(4, 'errand', '2023-11-02 20:40:18'),
(5, 'staff', '2023-11-02 20:40:51');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `store_name` int(11) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `contact` varchar(255) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_type` int(11) DEFAULT NULL,
  `role` varchar(255) NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `code` int(11) DEFAULT NULL,
  `verify` int(11) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `middle_name`, `last_name`, `sex`, `contact`, `email`, `password`, `user_type`, `role`, `image_url`, `code`, `verify`, `date_created`) VALUES
(5, 'Flynn', 'Quis magnam nulla mi', 'Bradshaw', 'Bradshaw', 'Irure veritatis ex q', 'doru@mailinator.com', 'sha256$3C19ILO74HCmxk1d$633f29c48c9ef08ba32b47bbe48d90cc97431a5a66909ca3708968f1a2b53523', 1, 'customer', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 19:24:15'),
(6, 'jay', 'jay', 'jay', 'jay', '1234567890-', 'jay@gmail.com', 'sha256$9DvXcp783Nn7FmRf$d9db69b6e23cff1c1f9dd56ec45b393374c5fa9996adf71e9b3e0098931acbd0', 1, 'customer', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 19:25:20'),
(7, 'mel', 'mel', 'mel', 'mel', '12345678', 'melriss@gmail.com', 'sha256$JsUbV8rWuz8v9ihB$d6281051aef2d0bc0e12709c85cc2a54ed98974b6ad7bd9e669102522151f598', 1, 'customer', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 19:47:15'),
(9, 'admin', 'admin', 'admin', 'admin', '12345678', 'admin@gmail.com', 'sha256$pkPDH9bt2KgiyaY2$c943c8e8f3b552a4efa69c02ee99520c7d75fe2c230811aee8bc25719aeaa95e', 2, 'admin', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 20:39:51'),
(11, 'Arnel', '', 'Maala', 'Maala', '12345678', 'arnel@gmail.com', 'sha256$3rFt2PFWP2cLMp20$75694313eda0dc2f0965def16f46eaaea00221cc3adc4040ee3b3ba56f0c3530', 3, 'vendor', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 20:46:26'),
(14, 'mel', 'm', 'mel', 'mel', '15678', 'mel@gmail.com', 'sha256$Gbqbd0UpQNIb9i8e$3074a35fc93c0e707f1c81fad9a9a3bdaf94a34b7c01c1caf2058cacc14d6d63', 3, 'vendor', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 21:03:16'),
(15, 'Yardley', 'Officia et rem deser', 'Silva', 'Silva', 'Commodo accusamus pe', 'cuduvydoz@mailinator.com', 'sha256$bZz4D1issGm9Ct4I$4c4bac5878d66ca0b30b8fbee52787fd3926c878044b01000a000ac517b1976d', 3, 'vendor', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-02 21:04:46'),
(16, 'Rosa', '', 'Estrada', 'Estrada', '09123456789', 'rosaapostol@gmail.com', 'sha256$kKRMRs5I9quh2yI2$6783d7b67c53b816dfff52112ee1146a9453365fa40f395b49cdcba1a1e15ab3', 1, 'customer', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-05 19:00:39'),
(17, 'nel', 'nel', 'nel', 'nel', '1234567', 'nel@gmail.com', 'sha256$lftQQFU8E0d0nzem$d29f59d2d55752abdc82b65eb76024d15f880e06cfcc6ac4cdd2e46ca7e148b9', 4, 'errand', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-06 21:41:18'),
(19, 'Jay', 'Agustin', 'Gonz', 'Gonz', '09123456789', 'jjj@gmail.com', 'sha256$Vaxpa9EDBDAUCBlr$ef939fc070caee4ec6f091f7ae4e586763a26b0da81c1647bf80d0e1090fd628', 1, 'customer', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-06 22:02:31'),
(21, 'junel', 'junel', 'junel', 'junel', '12345678', 'junel@gmail.com', 'sha256$Q0bzh7UBwAm1OiOS$97a006b84684f5242c8dded4404eca2816aa0601b6e832183fe7ab2c0dc9c027', 4, 'errand', 'https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png', 0, 0, '2023-11-09 21:36:15');

-- --------------------------------------------------------

--
-- Table structure for table `vendor`
--

CREATE TABLE `vendor` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `store_name` varchar(255) NOT NULL,
  `date_created` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vendor`
--

INSERT INTO `vendor` (`id`, `user_id`, `store_name`, `date_created`) VALUES
(1, 11, 'Arnel Store', '2023-11-02 20:46:26'),
(2, 14, 'Melriss Store', '2023-11-02 21:03:16'),
(3, 15, 'Bradley Mcfadden', '2023-11-02 21:04:46');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `complete__delivery`
--
ALTER TABLE `complete__delivery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `delivery`
--
ALTER TABLE `delivery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fee`
--
ALTER TABLE `fee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `food`
--
ALTER TABLE `food`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `remittance`
--
ALTER TABLE `remittance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `store_name` (`store_name`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `user_type` (`user_type`);

--
-- Indexes for table `vendor`
--
ALTER TABLE `vendor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT for table `complete__delivery`
--
ALTER TABLE `complete__delivery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `delivery`
--
ALTER TABLE `delivery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `fee`
--
ALTER TABLE `fee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `food`
--
ALTER TABLE `food`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `remittance`
--
ALTER TABLE `remittance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `vendor`
--
ALTER TABLE `vendor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `staff`
--
ALTER TABLE `staff`
  ADD CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `staff_ibfk_2` FOREIGN KEY (`store_name`) REFERENCES `vendor` (`id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`user_type`) REFERENCES `role` (`id`);

--
-- Constraints for table `vendor`
--
ALTER TABLE `vendor`
  ADD CONSTRAINT `vendor_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
