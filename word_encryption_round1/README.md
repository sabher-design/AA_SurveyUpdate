# Word Encryption Task

This is the [Word Encryption Task](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2503029) by Benndorf, Rau und Sölch (2014) implemented in o-Tree.

#### Description

The Word Encryption Task was first introduced by Erkal, Gangadharan and Nikiforakis (2011) in a paper on the effect of relative earnings on giving behaviour. In the original version, the participants were given a table which mapped letters to a number between 1 and 26. They then had to encrypt English words by substituting letters of the alphabet with numbers. Instead of entering for example the word “sports”, participants had to enter the sequence 13-16-21-2-19. Later, Benndorf, Rau and Sölch (2014) carefully modified the task by using three-letter nonsense sequences instead of existing words and by giving a new mapping of letters to numbers after every word. They let participants play 10 two-minute rounds to see how the performance increases over time.

For more details on the task, see p.28 here: https://www.uni-goettingen.de/de/document/download/8f5d4e7cd6d1ef3488df7a97340dbcb5-en.pdf/Minimizing%20Learning%20Behavior%20in%20Experiments%20with%20Repeated%20Real-Effort%20Tasks.pdf
##### Publication

Benndorf, V., Rau, H., & Sölch, C. (2014). Minimizing learning behavior in experiments with repeated real-effort tasks.


#### Requirement
* otree-core==1.3.7 (double check with our current version!)
* Django==1.8.8
* example_word_encryption.jpg

#### Setup

1. Copy the application folder to your otree project.
2. Add the application to your  `settings.py` 
3. `otree resetdb`
4. Run the below command to run the server on port 3000 on all of the interfaces:
`otree runserver 0.0.0.0:3000`

#### Key Variables
- *solved*: Number of correctly solved encryption problems
- *notSolved*: Number of encryption problems, that were not solved correctly
- *num_rounds*: Number of rounds
- *timeout_seconds*: Time per round
