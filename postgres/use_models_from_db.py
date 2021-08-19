import psycopg2

connection = psycopg2.connect(user='postgres',
                              password='admin',
                              host='localhost',
                              database='postgres')

cursor = connection.cursor()

select_query = "select * from modelstore.futurex_model_catalog"
models =cursor.execute(select_query)
models = cursor.fetchall()
models

classifier_from_db = pickle.loads(models[0][2])
scaler_from_db = pickle.loads(models[1][2])

new_pred = classifier_from_db.predict(scaler_from_db.transform(np.array([[40,20000]])))

new_pred_proba = classifier_from_db.predict_proba(scaler_from_db.transform(np.array([[40,20000]])))[:,1]
print(new_pred)
print(new_pred_proba)

new_pred = classifier_from_db.predict(scaler_from_db.transform(np.array([[42,50000]])))

new_pred_proba = classifier_from_db.predict_proba(scaler_from_db.transform(np.array([[42,50000]])))[:,1]
print(new_pred)
print(new_pred_proba)



