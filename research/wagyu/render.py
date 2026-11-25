from pathlib import Path
import cairosvg
from PIL import Image,ImageOps,ImageDraw
P=Path(__file__).resolve().parent;V=P/'visuals';thumbs=[]
for p in sorted(V.glob('*.svg')):
 out=p.with_suffix('.png');cairosvg.svg2png(url=str(p),write_to=str(out),output_width=1200)
 im=Image.open(out).convert('RGB');im.thumbnail((600,500));canvas=Image.new('RGB',(620,530),'#263646');canvas.paste(im,((620-im.width)//2,12));ImageDraw.Draw(canvas).text((14,510),p.stem,fill='white');thumbs.append(canvas)
board=Image.new('RGB',(1240,530*5),'#263646')
for i,im in enumerate(thumbs):board.paste(im,((i%2)*620,(i//2)*530))
board.save(V/'contact_sheet.png')
print('rendered',len(thumbs))
