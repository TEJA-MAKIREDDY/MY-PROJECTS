def login(self,username,password):

    with open("E-com_proj/user_reg.csv","r",newline='') as file:
        read=csv.DictReader(file)
        for row in read:
            if row["uname"]==username and row['pwd']==password:
                return True
    return False