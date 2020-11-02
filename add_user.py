#This file is run whenever you want to add a new user#Note this file does not interact with any other code -> it only changes the user.csv file to add a new userimport hashlibimport scrapeimport csv#function adds userdef add_user(first_name, last_name, phone_number, id, password):    classes = scrape.scrape(id, password)    with open('users.csv', 'a', newline='') as file:        writer = csv.writer(file)        #writer.writerow(["First Name", "Last Name", "Phone Number", "ID", "Password", "Classes"]) #-> this line is only used to create the table with the column titles        hashed_class_array = []        for i in classes:            name_of_class = i[0]            grade_in_class = i[1]            string_to_hash = name_of_class+grade_in_class            hashed_class = hashlib.sha1(string_to_hash.encode("UTF-8")).hexdigest()[:10] #hashes score and class            hashed_class_array.append(hashed_class)        writer.writerow([first_name, last_name, phone_number, id, password, hashed_class_array])