# ShibuyaUG

# 5/13/2021

# Stats are weird. You don't want to push your current/ max level past 100 because game isn't meant to be, but you can max your your luck to 999 at lvl 1. Unsure if it increases past that, don't see a point as that plus the stacking fights multiplies your drop rate so 999 is really all you need. Strength and Defense at 255 should be all you need but the person who helped me figure most of tis out stated they pushed these to the thousands but again, I don't see a reason to.

# Sync is a percentage! For Shiki, I have her sync set to 300% currently on my file. This value shows up as B8 0B in the file, and the decimal value is 3000, so keep that in mind when changing sync%. 

# Bravery is weird. The in game values at base level for each character are as follows: Neku=15, Shiki= 110, Joshua= 40, Beat=5. This is because their bravery is calculated as stat + (max level -1). In my file I was level 95, and her Bravery was at 204. In the file, her bravery showed up as 110. Beat's was 5 and Joshua's was 40. I recommend setting the value for their bravery as whatever you want the end result to be - 99 (for the leveling). 



Neku Current Level:

0x00000040

Neku Max Level: 

0x00000046

Neku EXP:

0x00000048 to 0x00000049


Neku ATK and Defense:

0x00000050 and 0x00000052

Neku Luck:

0x00000054

Neku Bravery:

0x00000056


Shiki ATK and Defense are 

0x0000007B and 0x0000007D

Shiki Sync is :

0x0000007f to 0x00000080

Shiki Bravery:

0x00000081 to 0x00000082

Joshua ATK and DEF are

0x00000095 and 0x00000097

Joshua Sync is 

0x00000099 to 0x0000009A

Joshua Bravery is 

0x0000009B to 0x0000009C


Beat atk and Def start at 

0x000000AF and 0x000000B1

Beat sync is 

0x000000B3 to 0x000000B4

Beat Bravery:

0x000000B5 to 0x000000B6


# Pins in your Stockpile are stored in the string XX XX YY 00 ZZ, Where XX is the pin's Hex id in little endian [so Pin 269 (Cure Drink)-1= 268 which in hex is 10C, but i the save file shows up as 0C 01], YY is the Pin's Level ( you can set this to whatever you like, if you set it to the pin's max level all you have to do is equip it and it'll be maxed out), and ZZ is the quantity (but You shouldn't change it as you can't have a stack of unmastered pins. or try it idk, I didn't risk it) 
# Stockpile is weird in that it is diagonal in the hex file, so where the first item in your stockpile is at 0x0137. the second pin is at 0x0146, and the third is on 0x0155 and so on. keep that in mind when editing a fresh file.


Start of Stockpile: 

0x00000137

End of Stockpile:

0x00000B7C
# (End of stockpile needs testing)



# Pins in your mastered Bank are stored in XX XX YY 00 RR RR 00 00 00 ZZ , Where XX XX is the pin's # -1 then converted to hex in little endian, YY is the level of the Pin (all pins here should be maxed out), RR RR is numbers that are random ( I just don't know what they're for and they don't seem to be stat related), and ZZ is how many you have. 
# The 500 Yen Pin is the first pin my save file received in the mastered bank (you receive it in the first fights, and you can't equip your current pins when you receive it so it is the first according to your save file). The  number for the 500 yen pin is 251 so minus 1 gives us 250. In little endian hex it looks like FA 00, it's max level is 2, and I currently have 99 of it which in hex is 63. The string for it in my save file looks like FA 00 02 00 01 00 00 00 00 63


Start of Mastered Bank:

0x00001037

End of Mastered Bank:

0x00001E16
# End of Mastered Bank: Can confirm,  your stockpile ends at 0x00001E16 if you have all 323 pins, even if you have all of them at 99

# Money is in addresses 

# 0x0000004C to 0x0000004E


# Update 7/13/2021

Found all threads, food, CD's, Stickers, Books, and crafting materials in the save file, wrote up their hex values. 
