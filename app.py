import datetime

def main():
    current_time = datetime.datetime.now()
    folder_name = current_time.strftime("%Y%m%d%H%M%S")
    
    print("Folder Name:", folder_name)
    # Rest of your application code goes here
    
if __name__ == "__main__":
    main()

