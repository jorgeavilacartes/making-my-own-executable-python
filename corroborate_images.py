from time import sleep

print("Cuenta regresiva:")

for j in range(3,0,-1):
    sleep(1)
    print("{}...".format(j))
    
print("Adios Roberto!")
sleep(2)





















# import pandas as pd
# from time import sleep

# def run():
    
#     filename="./files_list_s3_wrist_16bits_rescaled.csv"

#     table = pd.read_csv(filename)
#     print("table loaded")
#     print(table.head())
#     for j in range(5):
#         sleep(1)
#         print("Ha pasado {} segundos...".format(j))
        
#     print("Adios!")
#     print("Aqui con la Chimu UWU!!!!")

# if __name__ == "__main__":
#     run()