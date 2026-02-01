from moviepy.editor import TextClip, CompositeVideoClip

txt = TextClip("Hello Payal!", fontsize=70, color='white')
txt = txt.set_position("center").set_duration(5)

final = CompositeVideoClip([txt])
final.write_videofile("test_output.mp4", fps=24, codec="libx264")