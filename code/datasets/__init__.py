"""
The code is copyrighted by the authors. Permission to copy and use
this software for noncommercial use is hereby granted provided: (a)
this notice is retained in all copies, (2) the publication describing
the method (indicated below) is clearly cited, and (3) the
distribution from which the code was obtained is clearly cited. For
all other uses, please contact the authors.
 
The software code is provided "as is" with ABSOLUTELY NO WARRANTY
expressed or implied. Use at your own risk.

The code and the pre-trained deep neural network model provided with
this repository allow one to perform vessel detection in ultra-widefield
fundus photography images and to compute various evaluation metrics for 
the detected vessel maps by comparing these against provided ground 
truth. The ralated methodology and metrics are described in the paper:

L. Ding, A. E. Kuriyan, R. S. Ramchandran, C. C. Wykoff, and G. Sharma 
"Weakly-Supervised Vessel Detection in Ultra-Widefield Fundus Photography
Via Iterative Multi-Modal Registration and Learning", 
IEEE Trans. on Medical Imaging, 2020, accepted for publication, to appear.
"""
from .prime import PRIME_FP
from .patches import PatchData

