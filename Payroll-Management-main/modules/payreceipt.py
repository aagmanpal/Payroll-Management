from PIL import Image, ImageFont, ImageDraw

def payslip(empinfo, paygain, paydeduction, others):
    #empinfo = [employee ID, employee name, date and time, receipt no.]
    #paygain = [basic salary, bonus, other, gross salary]
    #paydeduction = [tax deduction, loans, fines, others, net deduction, net pay]
    #others = [payment mode, note]

    img = Image.open("assets/paysliptemp.png")
    i = ImageDraw.Draw(img)

    font = ImageFont.truetype("assets/Nunito-Regular.ttf", size = 50)
    
    #Empinfo
    i.text((223,405), f"{empinfo[0]}", fill = (0,0,0), font = font)
    i.text((226,575), f"{empinfo[1]}", fill = (0,0,0), font = font)
    i.text((913,405), f"{empinfo[2]}", fill = (0,0,0), font = font)
    i.text((913,575), f"{empinfo[3]}", fill = (0,0,0), font = font)

    #Details
    i.text((850,843), f"₹{paygain[0]}", fill = (0,0,0), font = font)
    i.text((850,938), f"₹{paygain[1]}", fill = (0,0,0), font = font)
    i.text((850,1033), f"₹{paygain[2]}", fill = (0,0,0), font = font)
    i.text((850,1128), f"₹{paygain[3]}", fill = (0,0,0), font = font)
    i.text((850,1320), f"-₹{paydeduction[0]}", fill = (0,0,0), font = font)
    i.text((850,1415), f"-₹{paydeduction[1]}", fill = (0,0,0), font = font)
    i.text((850,1511), f"-₹{paydeduction[2]}", fill = (0,0,0), font = font)
    i.text((850,1607), f"-₹{paydeduction[3]}", fill = (0,0,0), font = font)
    i.text((850,1703), f"-₹{paydeduction[4]}", fill = (0,0,0), font = font)
    i.text((850,1799), f"-₹{paydeduction[5]}", fill = (0,0,0), font = font)

    #Others
    i.text((228,2005), f"{others[0]}", fill = (0,0,0), font = font)
    i.text((924,2005), f"{others[1]}", fill = (0,0,0), font = font)

    img.save("receipt.png")