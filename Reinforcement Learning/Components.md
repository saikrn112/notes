slides: [here](https://drive.google.com/file/d/1jBAynNzOHIhhYNLsH5gAJX4E-EW84fRY/view?usp=sharing)

# Model
representation of world changes in response to agent's action
models 
- transition - predicts next state 
- reward - predicts immediate reward


# Policy ($\pi$)
function that is mapping agent's states to action


# Value function
future rewards from being in a state when following a particular policy
>expected discounted sum of future rewards under a particular policy $\pi$
$$
V^{\pi}(s_{t} = s) = \mathbb{E}_{\pi}[r_t + \gamma r_{t+1} + \gamma^{2} r_{t+2} + \gamma^{3} r_{t+3} + ...|s_{t} = s]
$$

>[!note] why $\gamma$?
>so that we can avoid reward going to infinity

>[!note] why giving more weightage for nearer terms? 
> didnt understand
>  ^pgzpixxd4


>[!question] What are we learning?
>we have 3 components but which component are we trying to learn? 
>are we trying to learn all of them or some of them? or is it a controllable parameter?

