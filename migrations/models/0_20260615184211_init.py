from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `author` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `age` INT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `publish` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `email` VARCHAR(32) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `book` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(32) NOT NULL,
    `price` INT NOT NULL,
    `img_url` VARCHAR(255),
    `bread` INT NOT NULL,
    `bcomment` INT NOT NULL,
    `publishs_id` INT NOT NULL,
    CONSTRAINT `fk_book_publish_8999eb74` FOREIGN KEY (`publishs_id`) REFERENCES `publish` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `book_author` (
    `book_id` INT NOT NULL,
    `author_id` INT NOT NULL,
    FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_book_author_book_id_818352` (`book_id`, `author_id`)
) CHARACTER SET utf8mb4 COMMENT='作者';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmW1P2zAQgP8K6icmdVMp7UD7lnZDY4wXAZsmAYqcxE2tOnZwnEGF8t9nOy9OkzQ05a"
    "2s/VLa813se3K+85mHlkcdiINPRsjHlLW+bD20CPCg+FIYaW+1gO9ruRRwYGGlCrSOFXAG"
    "bC6kI4ADKEQODGyGfI4oEVISYiyF1BaKiLhaFBJ0G0KTUxfyMZRruboRYkQceA+D9Kc/MU"
    "cIYmdmqciRcyu5yae+kh0SfqAU5WyWaVMcekQr+1OxZJJpI8Kl1IUEMsChfDxnoVy+XF3i"
    "Z+pRvFKtEi8xZ+PAEQgxz7m7IAObEslPrCZQDrpylo/dnd5eb3/3c29fqKiVZJK9KHZP+x"
    "4bKgInl61IjQMOYg2FUXNTf0vkhmPAqtGl+gV4YslFeCmqOnqpQOPTIfNM/Dxwb2JIXD4W"
    "P3e7NbB+G+fD78b59m73g/SFiiCOY/skGemqIclT8wNuBb65gZdoPx55KwLvGYJP7tjRJB"
    "d7UmABe3IHmGOWRmiXztMtD3ldrzKoLUonQfm1HAMyvaTyU72dQ+ErIHbVG0kS30A8Z5k3"
    "s2RSaF2HvVHfvg73O51+a6E3FKURlkr1ZMoHs5DKU48YxNKfbDhO3zEzyhTuCZymLM04YW"
    "ZvIhmKjZJBPmY0dMeZiS4IgquYG/I4sxgXQ+PrNyk3i6lWxYoHiNglTuJx1J5dekV1Sl2a"
    "X5usVGNTmVYsOdRVJo44blSaMoNNbYoJ+gzZTapTpr9O9SkPDHmuGTLcJOhyJkuFXbIp3y"
    "zquv3+AmEntObGnRqb5WgxCJpkvUx/XQPPsqnnwdjbRZnlTNYVmx9aGAXjwGxUYwtW6wSv"
    "dBgvsyyDPKAMIpccwUWPzWfxo1YTY82JmYG77PxWjJLKQ2z0Cr1M/mT+tG5GX+P8P/2M9q"
    "nY0egecLafmWlaih1Nrtl5Yj+jGNY3NOk2qehpcjtoflvj55Q2nc2KZdr25s7txfoa6AHU"
    "6JCeGawzwQYXcY/epA0Ss4Ojc5l2pXdzy86yl2hvdxSInli8a7O+AUWXXZn0k5HanA+0zi"
    "blv6OU/xeyINkliyatnMn7TFsvcrUgt0YDiIn6+wS40+ksAFBozQWoxmYBihl55U3Dj4vT"
    "k2qIOZMCyF9EOHjlIJu3t8RZlN+sJtYaitJruWgvCG5xHt72sfGnyHX483SgKNCAu0w9RT"
    "1g8Kr/56ooL9E/QZ4swQ=="
)
