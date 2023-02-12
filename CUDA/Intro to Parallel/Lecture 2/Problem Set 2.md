performing gaussian blur
converting AoS to SoA for faster cache lookup
perform the pixel wise computation per thread
it's simple `thread_id=block_dim*block_id + thread_id
load the image into block shared_memory
using gather op `many to one` 
	loop over filter multiplying weights and data
	populate the output

[CS344-Problem-Sets/student_func.cu at master · raoqiyu/CS344-Problem-Sets (github.com)](https://github.com/raoqiyu/CS344-Problem-Sets/blob/master/Problem%20Set%202/student_func.cu)
[udacity-IntroToParallelProgramming/student_func.cu at master · nickspell/udacity-IntroToParallelProgramming (github.com)](https://github.com/nickspell/udacity-IntroToParallelProgramming/blob/master/ProblemSet2-Blur/student_func.cu)

tiled convolution [217-lec8.pdf (ucr.edu)](http://www.cs.ucr.edu/~nael/217-f15/lectures/217-lec8.pdf)

