import random
import pandas as pd


def generateRelations(df_people, max_relations_per_person=1):
    person_ids = df_people['id'].tolist()
    
    df = pd.DataFrame(columns=['id1', 'id2'])

    for person in person_ids:
        for _ in range(random.randint(0, max_relations_per_person)):
            row = (person, random.choice(person_ids))
            if row[0] != row[1]:
                df = pd.concat([df, pd.DataFrame([row], columns=['id1', 'id2'])])
    return df

def generatePurchases(df_products, df_people, max_purchases=1):
    product_ids = df_products['id'].tolist()
    person_ids = df_people['id'].tolist()

    df = pd.DataFrame(columns=['person_id', 'product_id'])

    for person in person_ids:
        for _ in range(random.randint(0, max_purchases)):
            row = (person, random.choice(product_ids))
            df = pd.concat([df, pd.DataFrame([row], columns=['person_id', 'product_id'])])
    return df


def forGCN(num_nodes=1, max_num_edges_per=0):
    df = pd.DataFrame(columns=['id1', 'id2'])
    ids = list(range(0, num_nodes))
    for id in ids:
        for _ in range(random.randint(0, max_num_edges_per)):
            row = (id, random.choice(ids))
            if row[0] != row[1]:
                df = pd.concat([df, pd.DataFrame([row], columns=['id1', 'id2'])])
    df.to_csv('data/relations_gcn.csv', index=False)
    pd.DataFrame(ids, columns=['id']).to_csv('data/ids_gcn.csv', index=False)



def main():
    number_of_people = 20
    number_of_products = 15
    max_relations_per_person = 3
    max_purchases_per_person = 3

    df_people = pd.read_csv('data/5000people.csv', nrows=number_of_people)
    df_products = pd.read_csv('data/129products.csv', nrows=number_of_products)

    df_relations = generateRelations(df_people=df_people, max_relations_per_person=max_relations_per_person)
    df_relations.to_csv('data/relations.csv', index=False)

    df_purchases = generatePurchases(df_products=df_products, df_people=df_people, max_purchases=max_purchases_per_person)
    df_purchases.to_csv('data/purchases.csv', index=False)

    df_people.to_csv('data/people.csv', index=False)
    df_products.to_csv('data/products.csv', index=False)

    number_of_people = 20
    max_relations_per_person = 3

    forGCN(num_nodes=number_of_people, max_num_edges_per=max_relations_per_person)


if __name__ == '__main__':
    main()
