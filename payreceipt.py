from PIL import Image, ImageFont, ImageDraw

def payreceipt(empinfo, paygain, paydeduction, others):
    #empinfo = [employee ID, employee name, date and time, receipt no.]
    #paygain = [basic salary, bonus, other]
    #paydeduction = [tax deduction, health insurance, loans, fines, others]
    #others = [payment mode, note]
    
    gross_salary = float(paygain[0]) + float(paygain[1]) + float(paygain[2])
    deduction = float(paydeduction[0]) + float(paydeduction[1]) + float(paydeduction[2]) + float(paydeduction[3]) + float(paydeduction[4])
    net_pay = gross_salary - deduction

    img = Image.open("paysliptemp.png")
    i = ImageDraw.Draw(img)

    font = ImageFont.truetype("Nunito-Regular.ttf", size = 50)
    
    #Empinfo
    i.text((223,405), f"{empinfo[0]}", fill = (0,0,0), font = font)
    i.text((226,575), f"{empinfo[1]}", fill = (0,0,0), font = font)
    i.text((913,405), f"{empinfo[2]}", fill = (0,0,0), font = font)
    i.text((913,575), f"{empinfo[3]}", fill = (0,0,0), font = font)

    #Details
    i.text((850,843), f"₹{paygain[0]}", fill = (0,0,0), font = font)
    i.text((850,938), f"₹{paygain[1]}", fill = (0,0,0), font = font)
    i.text((850,1033), f"₹{paygain[2]}", fill = (0,0,0), font = font)
    i.text((850,1128), f"₹{gross_salary}", fill = (0,0,0), font = font)
    i.text((850,1320), f"-₹{paydeduction[0]}", fill = (0,0,0), font = font)
    i.text((850,1415), f"-₹{paydeduction[1]}", fill = (0,0,0), font = font)
    i.text((850,1511), f"-₹{paydeduction[2]}", fill = (0,0,0), font = font)
    i.text((850,1607), f"-₹{paydeduction[3]}", fill = (0,0,0), font = font)
    i.text((850,1703), f"-₹{paydeduction[4]}", fill = (0,0,0), font = font)
    i.text((850,1799), f"-₹{deduction}", fill = (0,0,0), font = font)
    i.text((850,1895), f"₹{net_pay}", fill = (0,0,0), font = font)

    #Others
    i.text((228,2095), f"{others[0]}", fill = (0,0,0), font = font)
    i.text((924,2095), f"{others[1]}", fill = (0,0,0), font = font)

    img.save("receipt.png")