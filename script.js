const canvas = document.querySelector("#trajectory-canvas");
const ctx = canvas.getContext("2d");

let width = 0;
let height = 0;
let ratio = 1;

function resize() {
  ratio = window.devicePixelRatio || 1;
  width = canvas.clientWidth;
  height = canvas.clientHeight;
  canvas.width = Math.floor(width * ratio);
  canvas.height = Math.floor(height * ratio);
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
}

function drawGrid() {
  ctx.strokeStyle = "rgba(242, 246, 240, 0.025)";
  ctx.lineWidth = 1;
  const step = 42;

  for (let x = 0; x < width; x += step) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.stroke();
  }

  for (let y = 0; y < height; y += step) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.stroke();
  }
}

function markerPosition(t) {
  const cx = width * 0.68;
  const cy = height * 0.48;
  const rx = Math.min(width * 0.2, 230);
  const ry = Math.min(height * 0.18, 140);
  return {
    x: cx + Math.sin(t) * rx,
    y: cy + Math.sin(t * 2) * ry,
  };
}

function drawTrajectory(t) {
  const points = [];
  for (let i = 0; i < 180; i += 1) {
    points.push(markerPosition(t - i * 0.035));
  }

  ctx.lineWidth = 2;
  for (let i = 1; i < points.length; i += 1) {
    const alpha = 1 - i / points.length;
    ctx.strokeStyle = `rgba(124, 246, 163, ${alpha * 0.28})`;
    ctx.beginPath();
    ctx.moveTo(points[i - 1].x, points[i - 1].y);
    ctx.lineTo(points[i].x, points[i].y);
    ctx.stroke();
  }

  const marker = points[0];
  const follower = {
    x: marker.x - 135,
    y: marker.y + 70,
  };

  ctx.strokeStyle = "rgba(104, 216, 255, 0.38)";
  ctx.setLineDash([8, 8]);
  ctx.beginPath();
  ctx.moveTo(follower.x, follower.y);
  ctx.lineTo(marker.x, marker.y);
  ctx.stroke();
  ctx.setLineDash([]);

  drawNode(marker.x, marker.y, 18, "#7cf6a3", "TAG");
  drawNode(follower.x, follower.y, 24, "#68d8ff", "UAV");
}

function drawNode(x, y, radius, color, label) {
  ctx.fillStyle = color;
  ctx.globalAlpha = 0.16;
  ctx.beginPath();
  ctx.arc(x, y, radius * 2.5, 0, Math.PI * 2);
  ctx.fill();
  ctx.globalAlpha = 1;

  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fill();

  ctx.fillStyle = "#06100b";
  ctx.font = "600 11px IBM Plex Mono, monospace";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(label, x, y);
}

function frame(ms) {
  const t = ms * 0.001;
  ctx.clearRect(0, 0, width, height);
  drawGrid();
  drawTrajectory(t);
  requestAnimationFrame(frame);
}

resize();
requestAnimationFrame(frame);
window.addEventListener("resize", resize);
