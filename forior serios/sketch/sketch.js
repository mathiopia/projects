
let time=0;
let wave=[];



function setup() {
slider=createSlider(1,50,1)
  createCanvas(1000, 500);

  
}

function draw() {
background(0)
translate(150,200)
noFill()

let x=0
let y=0
for (let i=0 ;i<slider.value();i++){
  let prev_x=x
  let prev_y=y
  let n=i+1;
// let radius=10*(4/(pow(n,2)) );
let radius1=20*(6/n*(pow(-1,i)));
x+=radius1*cos(n*time)

y+=radius1*sin(n*time)
// append(wave,x)
// append(wave,y)
stroke(255,100)

ellipse(prev_x,prev_y,2*radius1)
stroke(255)
line(prev_x,prev_y,x,y)}

wave.unshift(y)
fill(0,100,250)
ellipse(x,y,8)
translate(200,0)
line(x-200,y,0,wave[0])
beginShape()
noFill()
for (let i=1;i<wave.length;i++){
  vertex(i,wave[i]);
  // vertex(wave[i],i);
}
endShape()
if (wave.length>800){
  wave.pop()
}
  time+=0.05

  }



  

  

