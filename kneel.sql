CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
)

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL

)

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NUMERIC(5) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
)

Create Table `Orders`
(
	`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`style_id` INTEGER NOT NULL,
	`size_id` INTEGER NOT NULL,
	`metal_id` INTEGER NOT NULL,
	`time_stamp` NVARCHAR(160),
	FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
	FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
	FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)



)


drop TABLE Order; 

INSERT INTO `METALS` VALUES (null, 'gold', 454.56)
INSERT INTO `METALS` VALUES (null, 'silver', 344.56)
INSERT INTO `METALS` VALUES (null, 'bronze', 144.56)

INSERT INTO `STYLES` VALUES (null, 'classic', 34.45)
INSERT INTO `STYLES` VALUES (null, 'modern', 343.45)
INSERT INTO `STYLES` VALUES (null, 'vintage', 3433.45)

INSERT INTO `SIZES` VALUES (null, 'small', 3.33)
INSERT INTO `SIZES` VALUES (null, 'medium', 24.24)
INSERT INTO `SIZES` VALUES (null, 'large', 1324.24)






INSERT INTO `ORDERS` VALUES (null, 1, 2, 3, 'January 16th')
INSERT INTO `ORDERS` VALUES (null, 2, 1, 3, 'January 16th')

INSERT INTO `ORDERS` VALUES (null, 3, 1, 2, 'February 16th')
INSERT INTO `ORDERS` VALUES (null, 1, 2, 3, 'December 16th')
INSERT INTO `ORDERS` VALUES (null, 1, 2, 3, 'October 16th')
INSERT INTO `ORDERS` VALUES (null, 1, 2, 3, 'November 31st')
INSERT INTO `ORDERS` VALUES (null, 1, 2, 3, 'December 10th');


SELECT
    o.size_id,
    o.style_id,
    o.metal_id,
    o.time_stamp,
    m.metal,
    m.price,
    s.style,
    s.price,
    si.size,
    si.price
    -- You select the rest of the columns from the joined tables here
FROM `Orders` o
JOIN Metals m, Styles s, Sizes si ON m.id = o.metal_id AND s.id = o.style_id AND si.id = o.size_id

-- You write the rest of the JOIN clauses here







