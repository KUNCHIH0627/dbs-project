-- faqs 資料表（用 postgres 管理者帳號在 fastapi_dev 資料庫執行）
CREATE TABLE IF NOT EXISTS faqs (
    id         SERIAL PRIMARY KEY,
    course     VARCHAR(50)  NOT NULL,
    category   VARCHAR(50),
    question   VARCHAR(300) NOT NULL,
    answer     TEXT         NOT NULL,
    keywords   TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- API 最小授權：只給 CRUD 需要的權限
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE faqs TO dev_user;
GRANT USAGE, SELECT ON SEQUENCE faqs_id_seq TO dev_user;