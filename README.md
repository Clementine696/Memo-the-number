# Memo-the-number

## Description
- This program need PyQt5 to run

- ไฟล์จำเป็นที่ต้องมี
    มีรูปภาพที่จำเป็น 2 รูปคือ HowToPlay.jpg เพื่อใช้แสดงในหน้า How to play 
    และ Dogge.jpg สำหรับ  Icon สุดน่ารักของโปรแกรม
    
<br>

## How to play
This game is a memmory game.
1. Press start and remember the pattern of the blink.

(โปรแกรมนี้เป็นเกมสำหรับฝึกทักษะความจำ)
โดยมีขั้นตอนการเล่นดังนี้
1. กดปุ่ม start แล้วจดจำตำแหน่งของปุ่มที่กระพริบ
2. เมื่อหน้าจอแสดงคำว่า “Your turn!” ให้กดปุ่มที่กระพริบตามลำดับของการกระพริบ
โดยเมื่อกดปุ่มแล้ว จะหน่วงเวลา 1 วินาที จึงจะสามารถกดปุ่มต่อไปได้ โดยครั้งแรกจะมีปุ่มกระพริบ 3 ปุ่ม
การกระพริบแต่ละครั้งจะสุ่มปุ่มที่จะกระพริบ (สามารถกระพริบซ้ำช่องเดิมได้)
3. หากกดได้ถูกต้อง ให้กดปุ่ม continue โดยครั้งนี้จะเพิ่มจำนวนปุ่มที่กระพริบมาอีก 1 ปุ่ม
4. หากกดได้ถูกต้องจะทำตามข้อ 3 ไปเรื่อย ๆ
5. หากกดผิดเป็นอันจบเกม


รูปภาพของเกมส์
เมื่อเข้ามาหน้าแรกจะเจอกับการสอนเล่น และเมื่อกด play ก็จะไปหน้าตัวเกมส์

<p float="left">
    <img src="https://user-images.githubusercontent.com/53567265/210804959-9e5384f1-416a-4184-9459-eee4a51fbb41.png" width="600" />
    <img src="https://user-images.githubusercontent.com/53567265/211371362-a4b95e7a-0949-4adf-b646-d1f9c9f2c67e.png" width="250" />
</p>

เมื่อกด Start ตัวเกมส์จะกระพริบปุ่ม 3 ปุ่มให้เราจำว่าปุ่มอะไรและลำดับอะไรบ้าง

<p float="left">
  <img src="https://user-images.githubusercontent.com/53567265/210808712-1934cb65-0d74-4450-b57a-7c57f3aa8b05.png" width="250" />
  <img src="https://user-images.githubusercontent.com/53567265/210808800-756a5422-b6b9-454b-a2e8-23aae465231e.png" width="250" /> 
  <img src="https://user-images.githubusercontent.com/53567265/210808866-42cb6d5a-e2ac-4411-963f-4fd95ad45ab9.png" width="250" />
</p>

เมื่อกระพริบเสร็จแล้วก็จะเปลี่ยนเป็นคำว่า จากคำว่า Remember จะเปลี่ยนเป็นคำว่า Your turn

<img src="https://user-images.githubusercontent.com/53567265/210805120-a51e8e5f-ee04-41b3-a264-3452856c5acd.png" width="250" />

<br>



ละก็มาถึงตาของเราที่ต้องกดตาม 

<p float="left">
  <img src="https://user-images.githubusercontent.com/53567265/211361944-be2d31ab-4e2a-4d2a-b0cc-92fc7c863146.png" width="250" /> 
  <img src="https://user-images.githubusercontent.com/53567265/211361767-7df1166b-6b8c-4ef1-9867-4b21645afbec.png" width="250" />
  <img src="https://user-images.githubusercontent.com/53567265/211361797-d97a3065-b0f7-4fdf-bed7-eebeb39231e6.png" width="250" />
</p>
<br>

ละเมื่อเรากดเสร็จแบบถูกต้องตามลำดับก็จะได้คะแนนดังนั้น

<img src="https://user-images.githubusercontent.com/53567265/210805403-4ebec264-cb3c-42cb-9de9-1b5cc513034b.png" width="250" /> 

เมื่อกด continue ตัวเกมจะเพิ่มจำนวนเลขที่กระพริบไป 1 ตัว ซึ่งจะกลายเป็น 4 ตัว โดยที่ 3 ลำดับแรกยังคงเดิม
<p float="left">
  <img src="https://user-images.githubusercontent.com/53567265/211372752-78180c88-1754-4ec3-9d80-2f015e9a4be6.png" width="200" /> 
  <img src="https://user-images.githubusercontent.com/53567265/211372949-51007e4d-c785-4ae5-804c-b22b57f2c149.png" width="200" />
  <img src="https://user-images.githubusercontent.com/53567265/211372995-6a22fcf1-a7b6-4693-9cd0-f13c5d5dc763.png" width="200" />
  <img src="https://user-images.githubusercontent.com/53567265/211373040-f54ae59c-f699-454d-b719-965f90001f7c.png" width="200" />
</p>

ถ้าเล่นชนะอีก

<img src="https://user-images.githubusercontent.com/53567265/210805567-7a5c5076-8770-4139-a17b-23381da8e754.png" width="250" />

และถ้าหากรอบต่อไปเล่นแล้วกดปุ่มได้ไม่ถูก ก็จะขึ้นดังนี้ โดยที่ score ของเราจะยังขึ้นคงไว้ให้ดู และจะเริ่มนับจาก 0 ในเกมส์ต่อไป

<img src="https://user-images.githubusercontent.com/53567265/211373364-9eb560af-addb-4d02-9d39-fe59c2533ea7.png" width="250" />

