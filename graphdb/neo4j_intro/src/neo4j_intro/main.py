from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password12345")


def main() -> None:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    with driver.session() as session:
        result = session.run(
            """
            MATCH (u:User)-[:WORKS_AT]->(c:Company)
            RETURN u.name AS user_name, c.name AS company_name
            ORDER BY user_name
            """
        )

        for record in result:
            print(f"{record['user_name']} works at {record['company_name']}")

    driver.close()


if __name__ == "__main__":
    main()