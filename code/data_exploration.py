import mysql.connector as mycon
con=mycon.connect(host="localhost", user="root", passwd="dps@123", database='GMIS')
cur = con.cursor()

#Describing a function to insert records~
def insertMutation():
  print("Insert Mutation Record\n")
  mid = input("Enter Mutation ID: ")
  gene = input("Enter Gene Name: ")
  gene = gene.upper()
  while True:
    mtype = input("Enter Mutation Type (Substitution/Deletion/Insertion): ")
    mtype = mtype.capitalize()
    if mtype in ["Substitution", "Deletion", "Insertion"]:
      break
    else:
      print("Invalid Mutation Type! Try Again.")
  posn = int(input("Enter Mutation Position: "))
  disorder = input("Enter Associated Disorder: ")
  sign = input("Enter Clinical Significance (Benign/Pathogenic/Uncertain): ")
  sign = sign.capitalize()
  query = f"INSERT INTO MUTATION_DATA VALUES ('{mid}', '{gene}', '{mtype}', {posn}, '{disorder}', '{sign}');"
  cur.execute(query)
  con.commit()
  print("Mutation Record Inserted Successfully!\n")

#Describing a function to display all records~
def displayMutations():
  query = "SELECT * FROM MUTATION_DATA;"
  cur.execute()
  data = cur.fetchall()
  if data:
    print("~All Mutation Records~")
    for row in data:
      print(row)
  else:
    print("No Records Found.")

#Describing a function to search all records by gene~
def searchGene(gene):
  gene = gene.upper()
  query = f"SELECT * FROM MUTATION_DATA WHERE GENE_NAME='{gene}'"
  cur.execute(query)
  data = cur.fetchall()
  if data:
    for row in data:
      print(row)
  else:
    print("Gene Not Found.")

#Describing a function to update significance~
def updateSignificance(mid):
  new_sig = input("Enter New Clinical Significance: ")
  new_sig = new_sig.capitalize()
  query = f"UPDATE MUTATION_DATA SET CLINICAL_SIGNIFICANCE='{new_sig}' WHERE MUTATION_ID='{mid}'"
  cur.execute(query)
  con.commit()
  print("Clinical Significance Updated Successfully!")

#Describing a function to delete a record~
def deleteMutation(mid):
  query = f"DELETE FROM MUTATION_DATA WHERE MUTATION_ID='{mid}'"
  cur.execute(query)
  con.commit()
  print("Mutation Record Deleted Successfully!")

#Describing a function for Rule Based Risk Prediction~
def predictRisk(mid):
  query = f"SELECT CLINICAL_SIGNIFICANCE FROM MUTATION_DATA WHERE MUTATION_ID='{mid}'"
  cur.execute(query)
  data = cur.fetchone()
  if data:
    sign = data[0]
    if sign == "Pathogenic":
      print("High Risk Disorder Probability")
    elif sign == "Benign":
      print("Low Risk")
    else:
      print("Uncertain Risk -> Further Analysis Required")
  else:
    print("Mutation Not Found")

#main menu~
while True:
  print("0.Exit\n1. Insert Mutation Record\n2. Display All Mutations\n3. Search by Gene\n4. Update Clinical Significance\n5. Delete Mutation\n6. Predict Disorder Risk")
  choice = int(input("Enter choice: "))
  if choice == 1:
    insertMutation()
  elif choice == 2:
    displayMutations()
  elif choice == 3:
    gene = input("Enter Gene Name: ")
    searchGene(gene)
  elif choice == 4:
    mid = input("Enter Mutation ID: ")
    updateSignificance(mid)
  elif choice == 5:
    mid = input("Enter Mutation ID: ")
    deleteMutation(mid)
  elif choice == 6:
    mid = input("Enter Mutation ID: ")
    predictRisk(mid)
  elif choice == 0:
      print("Exiting...")
      break
  else:
      print("Invalid Choice!")
