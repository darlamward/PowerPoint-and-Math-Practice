# A yearly member receipt for St. John’s Marina & Yacht Club customers.
# Author: Darla Ward
# Date Completed: 05-26-2022

date = "2022-05-29"
HSTRate = .15
evenSiteCost = 80.00
oddSiteCost = 120.00
alternateMemberCost = 5.00
processingFee = 59.99
cancellationRate = .60

name = input("Enter Customer Name:")
streetAddress = input("Enter Street Address:")
city = input("Enter City:")
province = input("Enter Province:").upper()
zipCode = input("Enter Postal Code:").upper()
site = int(input("Enter site number(1-100):"))
phoneNum = input("Enter phone number:")
cellNum = input("Enter cell number:")
membership = input("Enter membership type(Standard(S) or Executive(E)):").upper()
alternateMembers = int(input("Enter amount of other members:"))
siteCleaning = input("Include weekly site cleaning(Yes(Y) or No(N))?").upper()
surveillance = input("Include video surveillance(Yes(Y) or No(N))?").upper()

if (site % 2) == 0:
    siteFee = evenSiteCost
else:
    siteFee = oddSiteCost
alternateMembersFee = alternateMembers * alternateMemberCost
siteCharge = siteFee + alternateMembersFee
if siteCleaning == "Y":
    siteCleaningCost = 50.00
else:
    siteCleaningCost = 0.00
if surveillance == "Y":
    surveillanceCost = 35.00
else:
    surveillanceCost = 0.00
extraCharges = siteCleaningCost + surveillanceCost
subtotal = siteFee + alternateMembersFee + extraCharges
salesTax = subtotal * HSTRate
totalMonthlyCharge = subtotal + salesTax
if membership == "S":
    monthlyDues = 75.00
else:
    monthlyDues = 150.00
totalMonthlyFees = totalMonthlyCharge + monthlyDues
totalYearlyFees = totalMonthlyFees * 12
monthlyPayment = (totalYearlyFees + processingFee) / 12
cancellationFee = (siteCharge * 12) * cancellationRate

siteChargeDsp = "${:,.2f}".format(siteCharge)
extraChargesDsp = "${:,.2f}".format(extraCharges)
subtotalDsp = "${:,.2f}".format(subtotal)
salesTaxDsp = "${:,.2f}".format(salesTax)
totalMonthlyChargeDsp = "${:,.2f}".format(totalMonthlyCharge)
monthlyDuesDsp = "${:,.2f}".format(monthlyDues)
totalMonthlyFeesDsp = "${:,.2f}".format(totalMonthlyFees)
totalYearlyFeesDsp = "${:,.2f}".format(totalYearlyFees)
monthlyPaymentDsp = "${:,.2f}".format(monthlyPayment)
cancellationFeeDsp = "${:,.2f}".format(cancellationFee)

print()
print()
print("{:^36}".format("St. John’s Marina & Yacht Club"))
print("{:^36}".format("Yearly Member Receipt"))
print("{:^36}".format("_" * 36))
print()
print("{:<36}".format("Client Name and Address:"))
print()
print("{:<24s}".format(name))
print("{:<24s}".format(streetAddress))
print("{:<s}, {:<2s} {:<6s}".format(city, province, zipCode))
print()
print("Phone: {:>10s} (H)".format(phoneNum))
print("       {:>10s} (C)".format(cellNum))
print()
if membership == "S":
    print("Site #: {:>3d}   Member type: {:>9s}".format(site, "STANDARD"))
else:
    print("Site #: {:>3d}   Member type: {:>9s}".format(site, "EXECUTIVE"))
print()
print("Alternative Members:              {:>2d}".format(alternateMembers))
if siteCleaning == "Y":
    print("Weekly site cleaning:            {:>3s}".format("Yes"))
else:
    print("Weekly site cleaning:            {:>3s}".format("No"))
if surveillance == "Y":
    print("Video surveillance:              {:>3s}".format("Yes"))
else:
    print("Video surveillance:              {:>3s}".format("No"))
print()
print("Site charges:              {:>9s}".format(siteChargeDsp))
print("Extra charges:               {:>7s}".format(extraChargesDsp))
print("{:>36}".format("-" * 13))
print("Subtotal:                  {:>9s}".format(subtotalDsp))
print("Sales tax (HST):             {:>7s}".format(salesTaxDsp))
print("{:>36}".format("-" * 13))
print("Total monthly charges:     {:>9s}".format(totalMonthlyChargeDsp))
print("Monthly dues:                {:>7s}".format(monthlyDuesDsp))
print("{:>36}".format("-" * 13))
print("Total monthly fees:        {:>9s}".format(totalMonthlyFeesDsp))
print("Total yearly fees:        {:>10s}".format(totalYearlyFeesDsp))
print()
print("Monthly payment:           {:>9s}".format(monthlyPaymentDsp))
print()
print("{:^36}".format("_" * 36))
print()
print("Issued: {:<10s}".format(date))
print("HST Reg No: 549-33-5849-4720-9885")
print()
print("Cancellation fee:          {:>9s}".format(cancellationFeeDsp))
