DROP TABLE IF EXISTS DDRequest;


CREATE TABLE DDRequest (
        DDRequestId SERIAL PRIMARY KEY,
        ESN TEXT,
        DDStatus TEXT,
        AccountId TEXT,
        Requestor TEXT,
        updated TIMESTAMP
    );