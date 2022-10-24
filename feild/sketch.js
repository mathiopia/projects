let point=[]
let multi=0.003
function setup() {
  createCanvas(windowWidth,windowHeight);
  angleMode(DEGREES)
  let desity=50
  let space=width/desity
  translate(width/2,height/2)
  for(let i=-width/2; i<width/2; i+=space){
    for(let j=-height/2; j<height/2; j+=space){
      let p=createVector(i,j)
      point.push(p)
    }
  }
}

function draw() {
  // background(255);
  colorMode(HSB)
  translate(width/2,height/2)

 
  noStroke()

  
  for(let i=0; i<point.length; i++){
    let slope1 = point[i].y
    let slope2 = 3 * point[i].x - point[i].y
    let slope = slope1 / slope2

  // let slope=(point[i].y*point[i].y)
    let mag=Math.sqrt(point[i].y*point[i].y+point[i].x*point[i].x)
    let hue=map(mag,0,height,0,360)
    fill(hue,255,255)
    // fill(0)
    // let angle = atan(slope)
    // let teta=map(angle,0,2,0,200)
    // console.log(angle)
    // let angle2=map(angle,88,90,0,6.28)
    let angle=map(noise(point[i].x*multi,point[i].y*multi),0,1,0,200)
    let vel=createVector(cos(angle),sin(angle))
    point[i].add(vel)
    // fill(0, 1)
    ellipse(point[i].x,point[i].y,1.5)
  }
}
function keyPressed(){
  if(key=='s'){
  save("my_feild.png");
  }

}
