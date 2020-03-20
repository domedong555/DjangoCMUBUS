# DjangoCMUBUS
  
กลุ่มคูโบต้า ได้ Review code ของกลุ่ม big O
  ***https://github.com/inzee86333/Miniprojact***  
  
พบว่ามี Code smell ประเภท BLOATER : Long method เพราะมี Method ชื่อเดียวกันและการทำงานคล้ายกันคือ courseName() courseDetail() coursePrice() อยู่ทั้งสามClass   
  ***Miniprojact/src/Course/MuscleBuilding.java***  
  ***Miniprojact/src/Course/WeightGain.java***  
  ***Miniprojact/src/Course/WeightLoss.java***  
  
ควรที่จะ Extract Method ทั้ง 3 Method ใน Class Course  
  ***Miniprojact/src/Course/Course.java***  
  
Code smell ของกลุ่มคูโบต้าคือ  
  1.ตรง data มีการใช้ซ้ำกัน ควรมีการประกาศไว้อีกที่หนึ้งให้เป็น global แล้วเรียกมาใช้ก็พอ  
  2.สร้าง data เปล่าๆมาแต่ไม่ได้ใช้  
