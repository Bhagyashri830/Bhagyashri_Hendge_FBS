#POGRAM TO WRITE MINIMUM NO OF NOTES FOR GIVRN AMOUNT
amount=int(input("enter the amount"))
 #500
 n500 =amount//500
 r_amount=amount%500
 #200
 n200=r_amount//200
 r_amount=r_amount%200
 #100
 n100=r_amount//100
 r_amount=r_amount%100
 #50
 n50=r_amount//50
 r_amount=r_amount%50
 #20
 n20=r_amount//20
 r_amount=r_amount%20
 #10
 n10=r_amount//10
 r_amonut=r_amount%10
  
  print("notes to be paid amount=",amount)
  
  print("note for 500=",n500)
  print("note for 200=",n200)
  print("note for 100=",n100)
  print("note for 50=",n50)
  print("note for 10=",n10)