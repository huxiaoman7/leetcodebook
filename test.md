<!DOCTYPE html>
<html>
<head>  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,height=device-height,initial-scale=1,user-scalable=0">
  <meta name="author" content="微信公众号：颜家大少">
  <meta name="email" content="3056432@qq.com">
  <meta name="description" content="一个Markdown在线转换工具，让Markdown内容，不需作任何调整就能同时在微信公众号、博客园、掘金、csdn等平台正确显示当前预览的效果">
  <title>Md2All export document</title>  
  <style type="text/css" id="markdown_preview_css"> 
 .output_wrapper pre code{font-family: Consolas, Inconsolata, Courier, monospace; display: block !important; white-space: pre !important; word-wrap: normal !important; word-break: normal !important;  overflow: auto !important;}  
.output_wrapper a:hover { text-decoration: underline; color: rgb(0, 96, 100); }
.output_wrapper figcaption { margin-top: 10px; text-align: center; color: rgb(153, 153, 153); font-size: 0.7em; }
.output_wrapper pre code .linenum { padding-right: 20px; word-spacing: 0px; }
.task-list-list { list-style-type: none; }
.task-list-list.checked { color: rgb(62, 62, 62); }
.task-list-list.uncheck { color: rgb(191, 193, 191); }
.task-list-list .icon_uncheck, .task-list-list .icon_check { display: inline-block; vertical-align: middle; margin-right: 10px; }
.task-list-list .icon_check::before { content: √; border: 2px solid rgb(62, 62, 62); color: red; }
.task-list-list .icon_uncheck::before { content: x; border: 2px solid rgb(191, 193, 191); color: rgb(191, 193, 191); }
.task-list-list .icon_check::before, .task-list-list .icon_uncheck::before { padding: 2px 8px 2px 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border-bottom-right-radius: 5px; border-bottom-left-radius: 5px; }
@font-face { font-family: KaTeX_AMS; src: url(https://md.aclickall.com/fonts/KaTeX_AMS-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_AMS-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_AMS-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Caligraphic; src: url(https://md.aclickall.com/fonts/KaTeX_Caligraphic-Bold.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Caligraphic-Bold.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Caligraphic-Bold.ttf) format(truetype); font-weight: bold; font-style: normal; }
@font-face { font-family: KaTeX_Caligraphic; src: url(https://md.aclickall.com/fonts/KaTeX_Caligraphic-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Caligraphic-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Caligraphic-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Fraktur; src: url(https://md.aclickall.com/fonts/KaTeX_Fraktur-Bold.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Fraktur-Bold.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Fraktur-Bold.ttf) format(truetype); font-weight: bold; font-style: normal; }
@font-face { font-family: KaTeX_Fraktur; src: url(https://md.aclickall.com/fonts/KaTeX_Fraktur-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Fraktur-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Fraktur-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Main; src: url(https://md.aclickall.com/fonts/KaTeX_Main-Bold.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Main-Bold.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Main-Bold.ttf) format(truetype); font-weight: bold; font-style: normal; }
@font-face { font-family: KaTeX_Main; src: url(https://md.aclickall.com/fonts/KaTeX_Main-BoldItalic.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Main-BoldItalic.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Main-BoldItalic.ttf) format(truetype); font-weight: bold; font-style: italic; }
@font-face { font-family: KaTeX_Main; src: url(https://md.aclickall.com/fonts/KaTeX_Main-Italic.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Main-Italic.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Main-Italic.ttf) format(truetype); font-weight: normal; font-style: italic; }
@font-face { font-family: KaTeX_Main; src: url(https://md.aclickall.com/fonts/KaTeX_Main-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Main-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Main-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Math; src: url(https://md.aclickall.com/fonts/KaTeX_Math-BoldItalic.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Math-BoldItalic.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Math-BoldItalic.ttf) format(truetype); font-weight: bold; font-style: italic; }
@font-face { font-family: KaTeX_Math; src: url(https://md.aclickall.com/fonts/KaTeX_Math-Italic.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Math-Italic.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Math-Italic.ttf) format(truetype); font-weight: normal; font-style: italic; }
@font-face { font-family: KaTeX_SansSerif; src: url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Bold.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Bold.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Bold.ttf) format(truetype); font-weight: bold; font-style: normal; }
@font-face { font-family: KaTeX_SansSerif; src: url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Italic.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Italic.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Italic.ttf) format(truetype); font-weight: normal; font-style: italic; }
@font-face { font-family: KaTeX_SansSerif; src: url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_SansSerif-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Script; src: url(https://md.aclickall.com/fonts/KaTeX_Script-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Script-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Script-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Size1; src: url(https://md.aclickall.com/fonts/KaTeX_Size1-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Size1-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Size1-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Size2; src: url(https://md.aclickall.com/fonts/KaTeX_Size2-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Size2-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Size2-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Size3; src: url(https://md.aclickall.com/fonts/KaTeX_Size3-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Size3-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Size3-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Size4; src: url(https://md.aclickall.com/fonts/KaTeX_Size4-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Size4-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Size4-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@font-face { font-family: KaTeX_Typewriter; src: url(https://md.aclickall.com/fonts/KaTeX_Typewriter-Regular.woff2) format(woff2), url(https://md.aclickall.com/fonts/KaTeX_Typewriter-Regular.woff) format(woff), url(https://md.aclickall.com/fonts/KaTeX_Typewriter-Regular.ttf) format(truetype); font-weight: normal; font-style: normal; }
@media screen { 
  .katex .mtable .vertical-separator { min-width: 1px; }
  .katex .mfrac .frac-line, .katex .overline .overline-line, .katex .underline .underline-line, .katex .hline, .katex .hdashline, .katex .rule { min-height: 1px; }
}
.katex-display { display: block; margin: 1em 0px; text-align: center; }
.katex-display > .katex { display: block; text-align: center; white-space: nowrap; }
.katex-display > .katex > .katex-html { display: block; }
.katex-display > .katex > .katex-html > .tag { position: absolute; right: 0px; }
.katex { font-style: normal; font-variant-caps: normal; font-weight: normal; font-stretch: normal; font-size: 1.21em; font-family: KaTeX_Main, "Times New Roman", serif; line-height: 1.2; text-indent: 0px; text-rendering: auto; }
.katex * { }
.katex .katex-mathml { position: absolute; clip: rect(1px, 1px, 1px, 1px); padding: 0px; border: 0px; height: 1px; width: 1px; overflow: hidden; }
.katex .katex-html { }
.katex .katex-html > .newline { display: block; }
.katex .base { position: relative; display: inline-block; white-space: nowrap; width: min-content; }
.katex .strut { display: inline-block; }
.katex .textbf { font-weight: bold; }
.katex .textit { font-style: italic; }
.katex .textrm { font-family: KaTeX_Main; }
.katex .textsf { font-family: KaTeX_SansSerif; }
.katex .texttt { font-family: KaTeX_Typewriter; }
.katex .mathit { font-family: KaTeX_Math; font-style: italic; }
.katex .mathrm { font-style: normal; }
.katex .mathbf { font-family: KaTeX_Main; font-weight: bold; }
.katex .boldsymbol { font-family: KaTeX_Math; font-weight: bold; font-style: italic; }
.katex .amsrm { font-family: KaTeX_AMS; }
.katex .mathbb, .katex .textbb { font-family: KaTeX_AMS; }
.katex .mathcal { font-family: KaTeX_Caligraphic; }
.katex .mathfrak, .katex .textfrak { font-family: KaTeX_Fraktur; }
.katex .mathtt { font-family: KaTeX_Typewriter; }
.katex .mathscr, .katex .textscr { font-family: KaTeX_Script; }
.katex .mathsf, .katex .textsf { font-family: KaTeX_SansSerif; }
.katex .mainit { font-family: KaTeX_Main; font-style: italic; }
.katex .mainrm { font-family: KaTeX_Main; font-style: normal; }
.katex .vlist-t { display: inline-table; table-layout: fixed; }
.katex .vlist-r { display: table-row; }
.katex .vlist { display: table-cell; vertical-align: bottom; position: relative; }
.katex .vlist > span { display: block; height: 0px; position: relative; }
.katex .vlist > span > span { display: inline-block; }
.katex .vlist > span > .pstrut { overflow: hidden; width: 0px; }
.katex .vlist-t2 { margin-right: -2px; }
.katex .vlist-s { display: table-cell; vertical-align: bottom; font-size: 1px; width: 2px; min-width: 2px; }
.katex .msupsub { text-align: left; }
.katex .mfrac > span > span { text-align: center; }
.katex .mfrac .frac-line { display: inline-block; width: 100%; border-bottom-style: solid; }
.katex .mspace { display: inline-block; }
.katex .llap, .katex .rlap, .katex .clap { width: 0px; position: relative; }
.katex .llap > .inner, .katex .rlap > .inner, .katex .clap > .inner { position: absolute; }
.katex .llap > .fix, .katex .rlap > .fix, .katex .clap > .fix { display: inline-block; }
.katex .llap > .inner { right: 0px; }
.katex .rlap > .inner, .katex .clap > .inner { left: 0px; }
.katex .clap > .inner > span { margin-left: -50%; margin-right: 50%; }
.katex .rule { display: inline-block; border: 0px solid; position: relative; }
.katex .overline .overline-line, .katex .underline .underline-line, .katex .hline { display: inline-block; width: 100%; border-bottom-style: solid; }
.katex .hdashline { display: inline-block; width: 100%; border-bottom-style: dashed; }
.katex .sqrt > .root { margin-left: 0.27777778em; margin-right: -0.55555556em; }
.katex .sizing, .katex .fontsize-ensurer { display: inline-block; }
.katex .sizing.reset-size1.size1, .katex .fontsize-ensurer.reset-size1.size1 { font-size: 1em; }
.katex .sizing.reset-size1.size2, .katex .fontsize-ensurer.reset-size1.size2 { font-size: 1.2em; }
.katex .sizing.reset-size1.size3, .katex .fontsize-ensurer.reset-size1.size3 { font-size: 1.4em; }
.katex .sizing.reset-size1.size4, .katex .fontsize-ensurer.reset-size1.size4 { font-size: 1.6em; }
.katex .sizing.reset-size1.size5, .katex .fontsize-ensurer.reset-size1.size5 { font-size: 1.8em; }
.katex .sizing.reset-size1.size6, .katex .fontsize-ensurer.reset-size1.size6 { font-size: 2em; }
.katex .sizing.reset-size1.size7, .katex .fontsize-ensurer.reset-size1.size7 { font-size: 2.4em; }
.katex .sizing.reset-size1.size8, .katex .fontsize-ensurer.reset-size1.size8 { font-size: 2.88em; }
.katex .sizing.reset-size1.size9, .katex .fontsize-ensurer.reset-size1.size9 { font-size: 3.456em; }
.katex .sizing.reset-size1.size10, .katex .fontsize-ensurer.reset-size1.size10 { font-size: 4.148em; }
.katex .sizing.reset-size1.size11, .katex .fontsize-ensurer.reset-size1.size11 { font-size: 4.976em; }
.katex .sizing.reset-size2.size1, .katex .fontsize-ensurer.reset-size2.size1 { font-size: 0.83333333em; }
.katex .sizing.reset-size2.size2, .katex .fontsize-ensurer.reset-size2.size2 { font-size: 1em; }
.katex .sizing.reset-size2.size3, .katex .fontsize-ensurer.reset-size2.size3 { font-size: 1.16666667em; }
.katex .sizing.reset-size2.size4, .katex .fontsize-ensurer.reset-size2.size4 { font-size: 1.33333333em; }
.katex .sizing.reset-size2.size5, .katex .fontsize-ensurer.reset-size2.size5 { font-size: 1.5em; }
.katex .sizing.reset-size2.size6, .katex .fontsize-ensurer.reset-size2.size6 { font-size: 1.66666667em; }
.katex .sizing.reset-size2.size7, .katex .fontsize-ensurer.reset-size2.size7 { font-size: 2em; }
.katex .sizing.reset-size2.size8, .katex .fontsize-ensurer.reset-size2.size8 { font-size: 2.4em; }
.katex .sizing.reset-size2.size9, .katex .fontsize-ensurer.reset-size2.size9 { font-size: 2.88em; }
.katex .sizing.reset-size2.size10, .katex .fontsize-ensurer.reset-size2.size10 { font-size: 3.45666667em; }
.katex .sizing.reset-size2.size11, .katex .fontsize-ensurer.reset-size2.size11 { font-size: 4.14666667em; }
.katex .sizing.reset-size3.size1, .katex .fontsize-ensurer.reset-size3.size1 { font-size: 0.71428571em; }
.katex .sizing.reset-size3.size2, .katex .fontsize-ensurer.reset-size3.size2 { font-size: 0.85714286em; }
.katex .sizing.reset-size3.size3, .katex .fontsize-ensurer.reset-size3.size3 { font-size: 1em; }
.katex .sizing.reset-size3.size4, .katex .fontsize-ensurer.reset-size3.size4 { font-size: 1.14285714em; }
.katex .sizing.reset-size3.size5, .katex .fontsize-ensurer.reset-size3.size5 { font-size: 1.28571429em; }
.katex .sizing.reset-size3.size6, .katex .fontsize-ensurer.reset-size3.size6 { font-size: 1.42857143em; }
.katex .sizing.reset-size3.size7, .katex .fontsize-ensurer.reset-size3.size7 { font-size: 1.71428571em; }
.katex .sizing.reset-size3.size8, .katex .fontsize-ensurer.reset-size3.size8 { font-size: 2.05714286em; }
.katex .sizing.reset-size3.size9, .katex .fontsize-ensurer.reset-size3.size9 { font-size: 2.46857143em; }
.katex .sizing.reset-size3.size10, .katex .fontsize-ensurer.reset-size3.size10 { font-size: 2.96285714em; }
.katex .sizing.reset-size3.size11, .katex .fontsize-ensurer.reset-size3.size11 { font-size: 3.55428571em; }
.katex .sizing.reset-size4.size1, .katex .fontsize-ensurer.reset-size4.size1 { font-size: 0.625em; }
.katex .sizing.reset-size4.size2, .katex .fontsize-ensurer.reset-size4.size2 { font-size: 0.75em; }
.katex .sizing.reset-size4.size3, .katex .fontsize-ensurer.reset-size4.size3 { font-size: 0.875em; }
.katex .sizing.reset-size4.size4, .katex .fontsize-ensurer.reset-size4.size4 { font-size: 1em; }
.katex .sizing.reset-size4.size5, .katex .fontsize-ensurer.reset-size4.size5 { font-size: 1.125em; }
.katex .sizing.reset-size4.size6, .katex .fontsize-ensurer.reset-size4.size6 { font-size: 1.25em; }
.katex .sizing.reset-size4.size7, .katex .fontsize-ensurer.reset-size4.size7 { font-size: 1.5em; }
.katex .sizing.reset-size4.size8, .katex .fontsize-ensurer.reset-size4.size8 { font-size: 1.8em; }
.katex .sizing.reset-size4.size9, .katex .fontsize-ensurer.reset-size4.size9 { font-size: 2.16em; }
.katex .sizing.reset-size4.size10, .katex .fontsize-ensurer.reset-size4.size10 { font-size: 2.5925em; }
.katex .sizing.reset-size4.size11, .katex .fontsize-ensurer.reset-size4.size11 { font-size: 3.11em; }
.katex .sizing.reset-size5.size1, .katex .fontsize-ensurer.reset-size5.size1 { font-size: 0.55555556em; }
.katex .sizing.reset-size5.size2, .katex .fontsize-ensurer.reset-size5.size2 { font-size: 0.66666667em; }
.katex .sizing.reset-size5.size3, .katex .fontsize-ensurer.reset-size5.size3 { font-size: 0.77777778em; }
.katex .sizing.reset-size5.size4, .katex .fontsize-ensurer.reset-size5.size4 { font-size: 0.88888889em; }
.katex .sizing.reset-size5.size5, .katex .fontsize-ensurer.reset-size5.size5 { font-size: 1em; }
.katex .sizing.reset-size5.size6, .katex .fontsize-ensurer.reset-size5.size6 { font-size: 1.11111111em; }
.katex .sizing.reset-size5.size7, .katex .fontsize-ensurer.reset-size5.size7 { font-size: 1.33333333em; }
.katex .sizing.reset-size5.size8, .katex .fontsize-ensurer.reset-size5.size8 { font-size: 1.6em; }
.katex .sizing.reset-size5.size9, .katex .fontsize-ensurer.reset-size5.size9 { font-size: 1.92em; }
.katex .sizing.reset-size5.size10, .katex .fontsize-ensurer.reset-size5.size10 { font-size: 2.30444444em; }
.katex .sizing.reset-size5.size11, .katex .fontsize-ensurer.reset-size5.size11 { font-size: 2.76444444em; }
.katex .sizing.reset-size6.size1, .katex .fontsize-ensurer.reset-size6.size1 { font-size: 0.5em; }
.katex .sizing.reset-size6.size2, .katex .fontsize-ensurer.reset-size6.size2 { font-size: 0.6em; }
.katex .sizing.reset-size6.size3, .katex .fontsize-ensurer.reset-size6.size3 { font-size: 0.7em; }
.katex .sizing.reset-size6.size4, .katex .fontsize-ensurer.reset-size6.size4 { font-size: 0.8em; }
.katex .sizing.reset-size6.size5, .katex .fontsize-ensurer.reset-size6.size5 { font-size: 0.9em; }
.katex .sizing.reset-size6.size6, .katex .fontsize-ensurer.reset-size6.size6 { font-size: 1em; }
.katex .sizing.reset-size6.size7, .katex .fontsize-ensurer.reset-size6.size7 { font-size: 1.2em; }
.katex .sizing.reset-size6.size8, .katex .fontsize-ensurer.reset-size6.size8 { font-size: 1.44em; }
.katex .sizing.reset-size6.size9, .katex .fontsize-ensurer.reset-size6.size9 { font-size: 1.728em; }
.katex .sizing.reset-size6.size10, .katex .fontsize-ensurer.reset-size6.size10 { font-size: 2.074em; }
.katex .sizing.reset-size6.size11, .katex .fontsize-ensurer.reset-size6.size11 { font-size: 2.488em; }
.katex .sizing.reset-size7.size1, .katex .fontsize-ensurer.reset-size7.size1 { font-size: 0.41666667em; }
.katex .sizing.reset-size7.size2, .katex .fontsize-ensurer.reset-size7.size2 { font-size: 0.5em; }
.katex .sizing.reset-size7.size3, .katex .fontsize-ensurer.reset-size7.size3 { font-size: 0.58333333em; }
.katex .sizing.reset-size7.size4, .katex .fontsize-ensurer.reset-size7.size4 { font-size: 0.66666667em; }
.katex .sizing.reset-size7.size5, .katex .fontsize-ensurer.reset-size7.size5 { font-size: 0.75em; }
.katex .sizing.reset-size7.size6, .katex .fontsize-ensurer.reset-size7.size6 { font-size: 0.83333333em; }
.katex .sizing.reset-size7.size7, .katex .fontsize-ensurer.reset-size7.size7 { font-size: 1em; }
.katex .sizing.reset-size7.size8, .katex .fontsize-ensurer.reset-size7.size8 { font-size: 1.2em; }
.katex .sizing.reset-size7.size9, .katex .fontsize-ensurer.reset-size7.size9 { font-size: 1.44em; }
.katex .sizing.reset-size7.size10, .katex .fontsize-ensurer.reset-size7.size10 { font-size: 1.72833333em; }
.katex .sizing.reset-size7.size11, .katex .fontsize-ensurer.reset-size7.size11 { font-size: 2.07333333em; }
.katex .sizing.reset-size8.size1, .katex .fontsize-ensurer.reset-size8.size1 { font-size: 0.34722222em; }
.katex .sizing.reset-size8.size2, .katex .fontsize-ensurer.reset-size8.size2 { font-size: 0.41666667em; }
.katex .sizing.reset-size8.size3, .katex .fontsize-ensurer.reset-size8.size3 { font-size: 0.48611111em; }
.katex .sizing.reset-size8.size4, .katex .fontsize-ensurer.reset-size8.size4 { font-size: 0.55555556em; }
.katex .sizing.reset-size8.size5, .katex .fontsize-ensurer.reset-size8.size5 { font-size: 0.625em; }
.katex .sizing.reset-size8.size6, .katex .fontsize-ensurer.reset-size8.size6 { font-size: 0.69444444em; }
.katex .sizing.reset-size8.size7, .katex .fontsize-ensurer.reset-size8.size7 { font-size: 0.83333333em; }
.katex .sizing.reset-size8.size8, .katex .fontsize-ensurer.reset-size8.size8 { font-size: 1em; }
.katex .sizing.reset-size8.size9, .katex .fontsize-ensurer.reset-size8.size9 { font-size: 1.2em; }
.katex .sizing.reset-size8.size10, .katex .fontsize-ensurer.reset-size8.size10 { font-size: 1.44027778em; }
.katex .sizing.reset-size8.size11, .katex .fontsize-ensurer.reset-size8.size11 { font-size: 1.72777778em; }
.katex .sizing.reset-size9.size1, .katex .fontsize-ensurer.reset-size9.size1 { font-size: 0.28935185em; }
.katex .sizing.reset-size9.size2, .katex .fontsize-ensurer.reset-size9.size2 { font-size: 0.34722222em; }
.katex .sizing.reset-size9.size3, .katex .fontsize-ensurer.reset-size9.size3 { font-size: 0.40509259em; }
.katex .sizing.reset-size9.size4, .katex .fontsize-ensurer.reset-size9.size4 { font-size: 0.46296296em; }
.katex .sizing.reset-size9.size5, .katex .fontsize-ensurer.reset-size9.size5 { font-size: 0.52083333em; }
.katex .sizing.reset-size9.size6, .katex .fontsize-ensurer.reset-size9.size6 { font-size: 0.5787037em; }
.katex .sizing.reset-size9.size7, .katex .fontsize-ensurer.reset-size9.size7 { font-size: 0.69444444em; }
.katex .sizing.reset-size9.size8, .katex .fontsize-ensurer.reset-size9.size8 { font-size: 0.83333333em; }
.katex .sizing.reset-size9.size9, .katex .fontsize-ensurer.reset-size9.size9 { font-size: 1em; }
.katex .sizing.reset-size9.size10, .katex .fontsize-ensurer.reset-size9.size10 { font-size: 1.20023148em; }
.katex .sizing.reset-size9.size11, .katex .fontsize-ensurer.reset-size9.size11 { font-size: 1.43981481em; }
.katex .sizing.reset-size10.size1, .katex .fontsize-ensurer.reset-size10.size1 { font-size: 0.24108004em; }
.katex .sizing.reset-size10.size2, .katex .fontsize-ensurer.reset-size10.size2 { font-size: 0.28929605em; }
.katex .sizing.reset-size10.size3, .katex .fontsize-ensurer.reset-size10.size3 { font-size: 0.33751205em; }
.katex .sizing.reset-size10.size4, .katex .fontsize-ensurer.reset-size10.size4 { font-size: 0.38572806em; }
.katex .sizing.reset-size10.size5, .katex .fontsize-ensurer.reset-size10.size5 { font-size: 0.43394407em; }
.katex .sizing.reset-size10.size6, .katex .fontsize-ensurer.reset-size10.size6 { font-size: 0.48216008em; }
.katex .sizing.reset-size10.size7, .katex .fontsize-ensurer.reset-size10.size7 { font-size: 0.57859209em; }
.katex .sizing.reset-size10.size8, .katex .fontsize-ensurer.reset-size10.size8 { font-size: 0.69431051em; }
.katex .sizing.reset-size10.size9, .katex .fontsize-ensurer.reset-size10.size9 { font-size: 0.83317261em; }
.katex .sizing.reset-size10.size10, .katex .fontsize-ensurer.reset-size10.size10 { font-size: 1em; }
.katex .sizing.reset-size10.size11, .katex .fontsize-ensurer.reset-size10.size11 { font-size: 1.19961427em; }
.katex .sizing.reset-size11.size1, .katex .fontsize-ensurer.reset-size11.size1 { font-size: 0.20096463em; }
.katex .sizing.reset-size11.size2, .katex .fontsize-ensurer.reset-size11.size2 { font-size: 0.24115756em; }
.katex .sizing.reset-size11.size3, .katex .fontsize-ensurer.reset-size11.size3 { font-size: 0.28135048em; }
.katex .sizing.reset-size11.size4, .katex .fontsize-ensurer.reset-size11.size4 { font-size: 0.32154341em; }
.katex .sizing.reset-size11.size5, .katex .fontsize-ensurer.reset-size11.size5 { font-size: 0.36173633em; }
.katex .sizing.reset-size11.size6, .katex .fontsize-ensurer.reset-size11.size6 { font-size: 0.40192926em; }
.katex .sizing.reset-size11.size7, .katex .fontsize-ensurer.reset-size11.size7 { font-size: 0.48231511em; }
.katex .sizing.reset-size11.size8, .katex .fontsize-ensurer.reset-size11.size8 { font-size: 0.57877814em; }
.katex .sizing.reset-size11.size9, .katex .fontsize-ensurer.reset-size11.size9 { font-size: 0.69453376em; }
.katex .sizing.reset-size11.size10, .katex .fontsize-ensurer.reset-size11.size10 { font-size: 0.83360129em; }
.katex .sizing.reset-size11.size11, .katex .fontsize-ensurer.reset-size11.size11 { font-size: 1em; }
.katex .delimsizing.size1 { font-family: KaTeX_Size1; }
.katex .delimsizing.size2 { font-family: KaTeX_Size2; }
.katex .delimsizing.size3 { font-family: KaTeX_Size3; }
.katex .delimsizing.size4 { font-family: KaTeX_Size4; }
.katex .delimsizing.mult .delim-size1 > span { font-family: KaTeX_Size1; }
.katex .delimsizing.mult .delim-size4 > span { font-family: KaTeX_Size4; }
.katex .nulldelimiter { display: inline-block; width: 0.12em; }
.katex .delimcenter { position: relative; }
.katex .op-symbol { position: relative; }
.katex .op-symbol.small-op { font-family: KaTeX_Size1; }
.katex .op-symbol.large-op { font-family: KaTeX_Size2; }
.katex .op-limits > .vlist-t { text-align: center; }
.katex .accent > .vlist-t { text-align: center; }
.katex .accent .accent-body:not(.accent-full) { width: 0px; }
.katex .accent .accent-body { position: relative; }
.katex .overlay { display: block; }
.katex .mtable .vertical-separator { display: inline-block; margin: 0px -0.025em; border-right-width: 0.05em; border-right-style: solid; }
.katex .mtable .vs-dashed { border-right-width: 0.05em; border-right-style: dashed; }
.katex .mtable .arraycolsep { display: inline-block; }
.katex .mtable .col-align-c > .vlist-t { text-align: center; }
.katex .mtable .col-align-l > .vlist-t { text-align: left; }
.katex .mtable .col-align-r > .vlist-t { text-align: right; }
.katex .svg-align { text-align: left; }
.katex svg, .screenShotTempCanvas { display: block; position: absolute; width: 100%; height: inherit; fill: currentcolor; stroke: currentcolor; fill-rule: nonzero; fill-opacity: 1; stroke-width: 1px; stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 4; stroke-dasharray: none; stroke-dashoffset: 0px; stroke-opacity: 1; }
.katex svg path { stroke: none; }
.katex .stretchy { width: 100%; display: block; position: relative; overflow: hidden; }
.katex .stretchy::before, .katex .stretchy::after { content: ""; }
.katex .hide-tail { width: 100%; position: relative; overflow: hidden; }
.katex .halfarrow-left { position: absolute; left: 0px; width: 50.2%; overflow: hidden; }
.katex .halfarrow-right { position: absolute; right: 0px; width: 50.2%; overflow: hidden; }
.katex .brace-left { position: absolute; left: 0px; width: 25.1%; overflow: hidden; }
.katex .brace-center { position: absolute; left: 25%; width: 50%; overflow: hidden; }
.katex .brace-right { position: absolute; right: 0px; width: 25.1%; overflow: hidden; }
.katex .x-arrow-pad { padding: 0px 0.5em; }
.katex .x-arrow, .katex .mover, .katex .munder { text-align: center; }
.katex .boxpad { padding: 0px 0.3em; }
.katex .fbox { box-sizing: border-box; border: 0.04em solid black; }
.katex .fcolorbox { box-sizing: border-box; border: 0.04em solid; }
.katex .cancel-pad { padding: 0px 0.2em; }
.katex .cancel-lap { margin-left: -0.2em; margin-right: -0.2em; }
.katex .sout { border-bottom-style: solid; border-bottom-width: 0.08em; } 
.output_wrapper .hljs{display: block; overflow-x: auto; padding: 0.5em; background-color: rgb(51, 51, 51); color: white; background-position: initial initial; background-repeat: initial initial;}

.output_wrapper .hljs-name,.output_wrapper  .hljs-strong{font-weight: bold;}

.output_wrapper .hljs-code,.output_wrapper  .hljs-emphasis{font-style: italic;}

.output_wrapper .hljs-tag{color: rgb(98, 200, 243);}

.output_wrapper .hljs-variable,.output_wrapper  .hljs-template-variable,.output_wrapper  .hljs-selector-id,.output_wrapper  .hljs-selector-class{color: rgb(173, 229, 252);}

.output_wrapper .hljs-string,.output_wrapper  .hljs-bullet{color: rgb(162, 252, 162);}

.output_wrapper .hljs-type,.output_wrapper  .hljs-title,.output_wrapper  .hljs-section,.output_wrapper  .hljs-attribute,.output_wrapper  .hljs-quote,.output_wrapper  .hljs-built_in,.output_wrapper  .hljs-builtin-name{color: rgb(255, 255, 170);}

.output_wrapper .hljs-number,.output_wrapper  .hljs-symbol,.output_wrapper  .hljs-bullet{color: rgb(211, 99, 99);}

.output_wrapper .hljs-keyword,.output_wrapper  .hljs-selector-tag,.output_wrapper  .hljs-literal{color: rgb(252, 194, 140);}

.output_wrapper .hljs-comment,.output_wrapper  .hljs-deletion,.output_wrapper  .hljs-code{color: rgb(136, 136, 136);}

.output_wrapper .hljs-regexp,.output_wrapper  .hljs-link{color: rgb(198, 180, 240);}

.output_wrapper .hljs-meta{color: rgb(252, 155, 155);}

.output_wrapper .hljs-deletion{background-color: rgb(252, 155, 155); color: rgb(51, 51, 51);}

.output_wrapper .hljs-addition{background-color: rgb(162, 252, 162); color: rgb(51, 51, 51);}

.output_wrapper .hljs a{color: inherit;}

.output_wrapper .hljs a:focus,.output_wrapper  .hljs a:hover{color: inherit; text-decoration: underline;}
 
.output_wrapper pre code {line-height: 18px; font-size: 14px; font-weight: normal; word-spacing: 0px; letter-spacing: 0px;} 
.output_wrapper{font-size: 16px; color: rgb(62, 62, 62); line-height: 1.6; word-spacing: 0px; letter-spacing: 0px; font-family: "Helvetica Neue", Helvetica, "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif;}

.output_wrapper *{font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;}

.output_wrapper p{margin: 1.5em 0px;}

.output_wrapper h1,.output_wrapper  h2,.output_wrapper  h3,.output_wrapper  h4,.output_wrapper  h5,.output_wrapper  h6{margin: 1.5em 0px; font-weight: bold;}

.output_wrapper h1{font-size: 1.6em;}

.output_wrapper h2{font-size: 1.4em;}

.output_wrapper h3{font-size: 1.3em;}

.output_wrapper h4{font-size: 1.2em;}

.output_wrapper h5{font-size: 1em;}

.output_wrapper h6{font-size: 1em;}

.output_wrapper h3{margin-bottom: 2em; margin-right: 5px; padding: 8px 15px; letter-spacing: 2px; background-image: linear-gradient(to right bottom, rgb(0, 188, 212), rgb(63, 81, 181)); background-color: rgb(63, 81, 181); color: rgb(255, 255, 255); border-left-width: 10px; border-left-style: solid; border-left-color: rgb(51, 51, 51); border-top-left-radius: 5px; border-top-right-radius: 5px; border-bottom-right-radius: 5px; border-bottom-left-radius: 5px; text-shadow: rgb(102, 102, 102) 1px 1px 1px; box-shadow: rgb(102, 102, 102) 1px 1px 2px;}

.output_wrapper ul,.output_wrapper  ol{padding-left: 32px;}

.output_wrapper ul{list-style-type: disc;}

.output_wrapper ol{list-style-type: decimal;}

.output_wrapper li *{}

.output_wrapper li{margin-bottom: 0.5em;}

.output_wrapper .code_size_default{line-height: 18px; font-size: 14px; font-weight: normal; word-spacing: 0px; letter-spacing: 0px;}

.output_wrapper .code_size_tight{line-height: 15px; font-size: 11px; font-weight: normal; word-spacing: -3px; letter-spacing: 0px;}

.output_wrapper pre code{font-family: Consolas, Inconsolata, Courier, monospace; border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px;}

.output_wrapper blockquote{display: block; padding: 15px 15px 15px 1rem; font-size: 0.9em; margin: 1em 0px; color: rgb(129, 145, 152); border-left-width: 6px; border-left-style: solid; border-left-color: rgb(220, 230, 240); background-color: rgb(242, 247, 251); overflow: auto; word-wrap: normal; word-break: normal; background-position: initial initial; background-repeat: initial initial;}

.output_wrapper blockquote p{margin: 0px;}

.output_wrapper a{text-decoration: none; color: rgb(30, 107, 184); word-wrap: break-word;}

.output_wrapper strong{font-weight: bold;}

.output_wrapper em{font-style: italic;}

.output_wrapper del{font-style: italic;}

.output_wrapper strong em{font-weight: bold;}

.output_wrapper hr{height: 1px; margin: 1.5rem 0px; border-style: dashed none none; border-top-width: 1px; border-top-color: rgb(165, 165, 165);}

.output_wrapper code{word-wrap: break-word; padding: 2px 4px; border-top-left-radius: 4px; border-top-right-radius: 4px; border-bottom-right-radius: 4px; border-bottom-left-radius: 4px; margin: 0px 2px; color: rgb(233, 105, 0); background-color: rgb(248, 248, 248); background-position: initial initial; background-repeat: initial initial;}

.output_wrapper img{display: block; margin: 0px auto; max-width: 100%;}

.output_wrapper figcaption{margin-top: 10px; text-align: center; color: rgb(153, 153, 153); font-size: 0.7em;}

.output_wrapper table{display: table; width: 100%; text-align: left;}

.output_wrapper tbody{border: 0px;}

.output_wrapper table tr{border-width: 1px 0px 0px; border-top-style: solid; border-top-color: rgb(204, 204, 204); background-color: white;}

.output_wrapper table tr th,.output_wrapper  table tr td{font-size: 1em; border: 1px solid rgb(204, 204, 204); padding: 0.5em 1em; text-align: left;}

.output_wrapper table tr th{font-weight: bold; background-color: rgb(240, 240, 240);}

.output_wrapper .katex-display{font-size: 1.22em;}

.output_wrapper .katex{padding: 8px 3px;}

.output_wrapper .katex-display > .katex{display: inline-block; text-align: center; padding: 3px;}

.output_wrapper .katex img{display: inline-block; vertical-align: middle;}

.output_wrapper a[href^="#"] sup{vertical-align: super; margin: 0px 2px; padding: 1px 3px; color: rgb(255, 255, 255); background-color: rgb(102, 102, 102); font-size: 0.7em; background-position: initial initial; background-repeat: initial initial;}

.output_wrapper .task-list-list{list-style-type: none;}

.output_wrapper .task-list-list.checked{color: rgb(62, 62, 62);}

.output_wrapper .task-list-list.uncheck{color: rgb(191, 193, 191);}

.output_wrapper .task-list-list .icon_uncheck,.output_wrapper  .task-list-list .icon_check{display: inline-block; vertical-align: middle; margin-right: 10px;}

.output_wrapper .task-list-list .icon_check::before{content: √; border: 2px solid rgb(62, 62, 62); color: red;}

.output_wrapper .task-list-list .icon_uncheck::before{content: x; border: 2px solid rgb(191, 193, 191); color: rgb(191, 193, 191);}

.output_wrapper .task-list-list .icon_check::before,.output_wrapper  .task-list-list .icon_uncheck::before{padding: 2px 8px 2px 5px; border-top-left-radius: 5px; border-top-right-radius: 5px; border-bottom-right-radius: 5px; border-bottom-left-radius: 5px;}

.output_wrapper .toc{margin-left: 25px;}

.output_wrapper .toc_item{display: block;}

.output_wrapper .toc_left{margin-left: 25px;}
 
</style>  
  <style type="text/css" id="export_setting_css">body { width: 100%; margin: 0px; padding: 0px; background-color: rgb(81, 154, 178); background-position: initial initial; background-repeat: initial initial; }
#export_content { margin: 40px 20%; padding: 20px; border: 1px solid rgb(149, 155, 111); background-color: rgb(255, 255, 255); background-position: initial initial; background-repeat: initial initial; }</style>  

</head><body><div id="export_content"><div class="output_wrapper" id="output_wrapper_id"><h2 id="hleetcodebook"><span># LeetCode-book</span></h2>
<h2 id="hleetcode1400"><span>- LeetCode 1~400题总结 + 专题知识点&amp;题型总结</span></h2>
<h2 id="hleetcode"><span>Leetcode知识点详解&amp;题型总结</span></h2>
<ul>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzI0OTQwMTA5Ng==&amp;mid=2247483811&amp;idx=1&amp;sn=f2861c24a58f7791cf1873817845bb5d&amp;chksm=e9935bc4dee4d2d22a5c38616152cf8f56650775d3fef932056002816468ae136d1b003a5f50&amp;token=968139680&amp;lang=zh_CN#rd">Leetcode专栏开始啦</a></li>
<li><a href="https://mp.weixin.qq.com/s?__biz=MzI0OTQwMTA5Ng==&amp;mid=2247483819&amp;idx=1&amp;sn=071731261441f702f429ae9fc1b98b84&amp;chksm=e9935bccdee4d2da68f0a62830c23daba65fe81c42f4f04f0f5358f1b76bcf144b70f3b4a30d&amp;token=1778626027&amp;lang=zh_CN#rd">Leetcode数组知识点&amp;题型总结</a><br>    - <a href="https://github.com/huxiaoman7/leetcodebook/blob/master/Array/array.md">github完整版文章</a></li>
<li><span>Leetcode链表知识点&amp;题型总结</span></li>
</ul>
<hr>
<h2 id="hleetcode-1"><span>LeetCode题目分类</span></h2>
<h3 id="h"><span>数组类题目</span></h3>
<h4 id="hksum"><span>K-SUM类题目</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="https://leetcode.com/problems/two-sum">Two   Sum    </a></td>
<td>easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>167</td>
<td><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted">Two Sum II - Input array is   sorted    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>15</td>
<td><a href="https://leetcode.com/problems/3sum">3Sum    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>16</td>
<td><a href="https://leetcode.com/problems/3sum-closest">3Sum   Closest    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>259</td>
<td><a href="https://leetcode.com/problems/3sum-smaller">3Sum   Smaller    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>18</td>
<td><a href="https://leetcode.com/problems/4sum">4Sum    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-1"><span>区间问题</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th style="text-align:left;">代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>56</td>
<td><a href="https://leetcode.com/problems/merge-intervals">Merge   Intervals    </a></td>
<td>Medium</td>
<td style="text-align:left;">python、java、c++</td>
</tr>
<tr>
<td>57</td>
<td><a href="https://leetcode.com/problems/insert-interval">Insert   Interval    </a></td>
<td>Hard</td>
<td style="text-align:left;">python、java、c++</td>
</tr>
<tr>
<td>252</td>
<td><a href="https://leetcode.com/problems/meeting-rooms/">Meeting Rooms</a></td>
<td>easy</td>
<td style="text-align:left;">python、java、c++</td>
</tr>
<tr>
<td>253</td>
<td><a href="https://leetcode.com/problems/meeting-rooms-ii/">Meeting Rooms II</a></td>
<td>medium</td>
<td style="text-align:left;">python、java、c++</td>
</tr>
<tr>
<td>352</td>
<td><a href="https://leetcode.com/problems/data-stream-as-disjoint-intervals/">Data   Stream as Disjoint Intervals</a></td>
<td>hard</td>
<td style="text-align:left;">python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-2"><span>子数组类题目</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>78</td>
<td><a href="https://leetcode.com/problems/subsets/">Subsets</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>90</td>
<td><a href="https://leetcode.com/problems/subsets-ii/">Subsets II</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>53</td>
<td><a href="https://leetcode.com/problems/maximum-subarray/">Maximum Subarray</a></td>
<td>easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>152</td>
<td><a href="https://leetcode.com/problems/maximum-product-subarray/">Maximum Product Subarray</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>239</td>
<td><a href="https://leetcode.com/problems/sliding-window-maximum/">Sliding Window   Maximum</a></td>
<td>hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>295</td>
<td><a href="https://leetcode.com/problems/find-median-from-data-stream/">Find   Median from Data Stream</a></td>
<td>hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>228</td>
<td><a href="https://leetcode.com/problems/summary-ranges/">Summary Ranges</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>163</td>
<td><a href="https://leetcode.com/problems/missing-ranges/">Missing Ranges</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>325</td>
<td><a href="https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/">Maximum   Size Subarray Sum Equals k</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>209</td>
<td><a href="https://leetcode.com/problems/minimum-size-subarray-sum/">Minimum Size   Subarray Sum</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>238</td>
<td><a href="https://leetcode.com/problems/product-of-array-except-self/">Product   of Array Except Self</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>128</td>
<td><a href="https://leetcode.com/problems/longest-consecutive-sequence">Longest Consecutive Sequence    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="hrotate"><span>Rotate类题目</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>48</td>
<td><a href="https://leetcode.com/problems/rotate-image">Rotate Image    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>89</td>
<td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array">Search in Rotated   Sorted Array    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>189</td>
<td><a href="https://leetcode.com/problems/rotate-array">Rotate Array    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>81</td>
<td><a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii">Search in Rotated   Sorted Array II    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-3"><span>数组排序</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>88</td>
<td><a href="https://leetcode.com/problems/merge-sorted-array">Merge Sorted Array    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>75</td>
<td><a href="https://leetcode.com/problems/sort-colors">Sort   Colors    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>283</td>
<td><a href="https://leetcode.com/problems/move-zeroes">Move   Zeroes    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>376</td>
<td><a href="https://leetcode.com/problems/wiggle-subsequence/">Wiggle Subsequence</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>280</td>
<td><a href="https://leetcode.com/problems/wiggle-sort/">Wiggle Sort</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>324</td>
<td><a href="https://leetcode.com/problems/wiggle-sort-ii/">Wiggle Sort II</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>215</td>
<td><a href="https://leetcode.com/problems/kth-largest-element-in-an-array">Kth Largest Element in an Array   </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>287</td>
<td><a href="https://leetcode.com/problems/find-the-duplicate-number">Find the Duplicate Number</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>334</td>
<td><a href="https://leetcode.com/problems/increasing-triplet-subsequence">Increasing Triplet Subsequence   </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>400</td>
<td><a href="https://leetcode.com/problems/nth-digit">Nth Digit  </a></td>
<td>easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>387</td>
<td><a href="https://leetcode.com/problems/first-unique-character-in-a-string">First Unique Character in a String   </a></td>
<td>easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>164</td>
<td><a href="https://leetcode.com/problems/maximum-gap">Maximum Gap    </a></td>
<td>hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>347</td>
<td><a href="https://leetcode.com/problems/top-k-frequent-elements">Top K Frequent Elements    </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>243</td>
<td><a href="https://leetcode.com/problems/shortest-word-distance">Shortest Word Distance</a></td>
<td>easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>244</td>
<td><a href="https://leetcode.com/problems/shortest-word-distance-ii">Shortest Word Distance II </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>245</td>
<td><a href="https://leetcode.com/problems/shortest-word-distance-iii">Shortest Word Distance III</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-4"><span>双指针问题</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>11</td>
<td><a href="https://leetcode.com/problems/container-with-most-water">Container With Most Water    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>41</td>
<td><a href="https://leetcode.com/problems/first-missing-positive">First Missing Positive    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>42</td>
<td><a href="https://leetcode.com/problems/trapping-rain-water">Trapping Rain Water    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>84</td>
<td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram">Largest Rectangle in Histogram    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>85</td>
<td><a href="https://leetcode.com/problems/maximal-rectangle">Maximal Rectangle    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>243</td>
<td><a href="https://leetcode.com/problems/shortest-word-distance">Shortest Word Distance    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>244</td>
<td><a href="https://leetcode.com/problems/shortest-word-distance-ii">Shortest Word Distance II</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>245</td>
<td><a href="https://leetcode.com/problems/shortest-word-distance-iii">Shortest Word Distance III    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-5"><span>二维数组</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>48</td>
<td><a href="https://leetcode.com/problems/rotate-image">Rotate   Image    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>54</td>
<td><a href="https://leetcode.com/problems/spiral-matrix">Spiral   Matrix    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>73</td>
<td><a href="https://leetcode.com/problems/set-matrix-zeroes">Set Matrix Zeroes    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>311</td>
<td><a href="https://leetcode.com/problems/sparse-matrix-multiplication">Sparse Matrix   Multiplication    </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>36</td>
<td><a href="https://leetcode.com/problems/valid-sudoku">Valid Sudoku </a></td>
<td>meidum</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>37</td>
<td><a href="https://leetcode.com/problems/sudoku-solver">Sudoku Solver  </a></td>
<td>hard</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-6"><span>动态规划</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>62</td>
<td><a href="https://leetcode.com/problems/unique-paths">Unique Paths    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>63</td>
<td><a href="https://leetcode.com/problems/unique-paths-ii">Unique Paths II    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>64</td>
<td><a href="https://leetcode.com/problems/minimum-path-sum">Minimum Path Sum    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>120</td>
<td><a href="https://leetcode.com/problems/triangle">Triangle    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-7"><span>二叉树</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>105</td>
<td><a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal">Construct Binary   Tree from Preorder and Inorder Traversal    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>106</td>
<td><a href="https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal">Construct Binary   Tree from Inorder and Postorder Traversal    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="hmath"><span>Math</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>66</td>
<td><a href="https://leetcode.com/problems/plus-one">Plus   One    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>118</td>
<td><a href="https://leetcode.com/problems/pascals-triangle">Pascal's Triangle    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>119</td>
<td><a href="https://leetcode.com/problems/pascals-triangle-ii">Pascal's Triangle II    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-8"><span>基础</span></h4>
<h5 id="h-9"><span>基础题目</span></h5>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>217</td>
<td><a href="https://leetcode.com/problems/contains-duplicate">Contains Duplicate    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>219</td>
<td><a href="https://leetcode.com/problems/contains-duplicate-ii">Contains Duplicate II    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>380</td>
<td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1">Insert Delete   GetRandom O(1)    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>381</td>
<td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed">Insert Delete   GetRandom O(1) - Duplicates allowed    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>31</td>
<td><a href="https://leetcode.com/problems/next-permutation">Next Permutation    </a></td>
<td>Medium</td>
<td></td>
</tr>
</tbody>
</table>
<h5 id="hsearch"><span>Search类题</span></h5>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>33</td>
<td><a href="https://leetcode.com/problems/wiggle-subsequence/">Search in Rotated Sorted Array    </a></td>
<td>Medium</td>
<td>代码</td>
</tr>
<tr>
<td>81</td>
<td><a href="https://leetcode.com/problems/sort-colors">Search   in Rotated Sorted Array II    </a></td>
<td>Medium</td>
<td></td>
</tr>
<tr>
<td>34</td>
<td><a href="https://leetcode.com/problems/wiggle-sort/">Find First and Last Position of Element in Sorted   Array    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>35</td>
<td><a href="https://leetcode.com/problems/next-permutation">Search Insert Position    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>74</td>
<td><a href="https://leetcode.com/problems/combination-sum">Search a 2D Matrix    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>79</td>
<td><a href="https://leetcode.com/problems/combination-sum-ii">Word Search    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>153</td>
<td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array">Find Minimum in Rotated Sorted   Array    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>154</td>
<td><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii">Find Minimum in Rotated Sorted Array   II    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>39</td>
<td><a href="https://leetcode.com/problems/largest-rectangle-in-histogram">Combination   Sum    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>40</td>
<td><a href="https://leetcode.com/problems/combination-sum-ii">Combination Sum II    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>216</td>
<td><a href="https://leetcode.com/problems/combination-sum-iii">Combination Sum III    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>45</td>
<td><a href="https://leetcode.com/problems/jump-game-ii">Jump   Game II    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>55</td>
<td><a href="https://leetcode.com/problems/jump-game">Jump   Game    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>121</td>
<td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock">Best Time to Buy and   Sell Stock    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>122</td>
<td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii">Best Time to Buy and   Sell Stock II    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>123</td>
<td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii">Best Time to Buy and   Sell Stock III    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>126</td>
<td><a href="https://leetcode.com/problems/word-ladder-ii">Word   Ladder II    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>162</td>
<td><a href="https://leetcode.com/problems/find-peak-element">Find Peak Element    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>169</td>
<td><a href="https://leetcode.com/problems/majority-element">Majority Element    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>229</td>
<td><a href="https://leetcode.com/problems/majority-element-ii">Majority Element II    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h5 id="hremove"><span>Remove类题目</span></h5>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>26</td>
<td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">Remove Duplicates from Sorted   Array    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>27</td>
<td><a href="https://leetcode.com/problems/remove-element">Remove   Element    </a></td>
<td>Easy</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>80</td>
<td><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii">Remove Duplicates from Sorted Array   II    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-10"><span>提高题目</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>4</td>
<td><a href="https://leetcode.com/problems/median-of-two-sorted-arrays">Median of Two Sorted Arrays    </a></td>
<td>Hard</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>289</td>
<td><a href="https://leetcode.com/problems/game-of-life">Game   of Life    </a></td>
<td>Medium</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table>
<h4 id="h-11"><span>综合题</span></h4>
<table>
<thead>
<tr>
<th>序号</th>
<th>题目</th>
<th>难度</th>
<th>代码</th>
</tr>
</thead>
<tbody>
<tr>
<td>274</td>
<td><a href="https://leetcode.com/problems/h-index/">H-Index</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>376</td>
<td><a href="https://leetcode.com/problems/wiggle-subsequence">Wiggle Subsequence</a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>277</td>
<td><a href="https://leetcode.com/problems/game-of-life">Find the Celebrity    </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>370</td>
<td><a href="https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed">Range   Addition    </a></td>
<td>medium</td>
<td>python、java、c++</td>
</tr>
<tr>
<td>296</td>
<td><a href="https://leetcode.com/problems/best-meeting-point">Best Meeting Point</a></td>
<td>hard</td>
<td>python、java、c++</td>
</tr>
</tbody>
</table></div></div></body>
</html>
