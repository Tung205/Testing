def tuyenSinh(thpt, hoc_ba, sat):
    if (thpt < 0 or thpt > 30):
        return "Error"
    if (hoc_ba < 0 or hoc_ba > 10):
        return "Error"
    if (sat < 0 or sat > 1600):
        return "Error"
    if (thpt < 22 or hoc_ba < 8 or sat < 1300):
        return "Rejected"
    else:
        if (thpt < 26 or hoc_ba < 9 or sat < 1450):
            return "Waitlisted"
    return "Accepted"

def main():
    thpt = float(input("Enter thpt (0-30): "))
    hoc_ba = float(input("Enter hoc_ba (0-10): "))
    sat = int(input("Enter sat (0-1600): "))
    
    result = tuyenSinh(thpt, hoc_ba, sat)
    print(result)

if __name__ == "__main__":
    main()

