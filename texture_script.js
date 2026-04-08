
// --- PROCEDURAL TEXTURES ---
const textures = {};
function initTextures() {
  const mkCanvas = (s) => { const c=document.createElement('canvas'); c.width=c.height=s; return [c, c.getContext('2d')]; };

  // Grass Texture
  const [cg, ctxg] = mkCanvas(128);
  ctxg.fillStyle = '#4a7c3f'; ctxg.fillRect(0,0,128,128);
  for(let i=0;i<400;i++){
    ctxg.fillStyle = Math.random()>0.5 ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)';
    const x=Math.random()*128, y=Math.random()*128;
    ctxg.fillRect(x,y,2,Math.random()*6+2);
  }
  textures.grass = ctx.createPattern(cg, 'repeat');

  // Pavement Texture
  const [cp, ctxp] = mkCanvas(128);
  ctxp.fillStyle = '#8e9eab'; ctxp.fillRect(0,0,128,128);
  for(let i=0;i<1000;i++){
    ctxp.fillStyle = `rgba(${Math.random()*50},${Math.random()*50},${Math.random()*50},0.05)`;
    ctxp.fillRect(Math.random()*128,Math.random()*128,1,1);
  }
  // Subtle pavement cracks/lines
  ctxp.strokeStyle='rgba(0,0,0,0.03)'; ctxp.lineWidth=1;
  ctxp.beginPath(); ctxp.moveTo(0,0); ctxp.lineTo(128,128); ctxp.stroke();
  textures.pavement = ctx.createPattern(cp, 'repeat');

  // Wood Texture
  const [cw, ctxw] = mkCanvas(256);
  ctxw.fillStyle = '#c8832c'; ctxw.fillRect(0,0,256,256);
  ctxw.strokeStyle = 'rgba(0,0,0,0.05)';
  for(let i=0;i<256;i+=4){
    ctxw.lineWidth = Math.random()*2+1;
    ctxw.beginPath(); ctxw.moveTo(i,0); ctxw.lineTo(i+Math.random()*10-5,256); ctxw.stroke();
  }
  for(let i=0;i<256;i+=32){
    ctxw.strokeStyle='rgba(0,0,0,0.2)'; ctxw.lineWidth=1;
    ctxw.beginPath(); ctxw.moveTo(i,0); ctxw.lineTo(i,256); ctxw.stroke();
  }
  textures.wood = ctx.createPattern(cw, 'repeat');

  // Blue Court Texture (Pickleball)
  const [cb, ctxb] = mkCanvas(128);
  ctxb.fillStyle = '#1e6fa0'; ctxb.fillRect(0,0,128,128);
  for(let i=0;i<800;i++){
    ctxb.fillStyle = `rgba(255,255,255,0.03)`;
    ctxb.fillRect(Math.random()*128,Math.random()*128,2,2);
  }
  textures.courtBlue = ctx.createPattern(cb, 'repeat');

  // Red Court Texture (Pickleball Kitchen)
  const [cr, ctxr] = mkCanvas(128);
  ctxr.fillStyle = '#c0392b'; ctxr.fillRect(0,0,128,128);
  for(let i=0;i<800;i++){
    ctxr.fillStyle = `rgba(0,0,0,0.04)`;
    ctxr.fillRect(Math.random()*128,Math.random()*128,2,2);
  }
  textures.courtRed = ctx.createPattern(cr, 'repeat');
}
