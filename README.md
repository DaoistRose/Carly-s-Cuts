# Carly-s-Cuts

### My Beginner’s Journey (Part 4)

When I first opened up the Carly’s Clippers project, it felt refreshingly manageable: simple lists, basic math, and just a few loops. But, as I’ve learned on this Python path, simplicity can still hold plenty of struggle. This project gave me a great chance to practice core concepts like list iteration, list comprehensions, and working with indexes—and reminded me that even when the path is straightforward, it’s okay to walk it slowly.

---

## Getting Started

I’m currently at Day 8 of my Beginner Python 3 Codecademy journey. For this assignment, I stepped into the role of data analyst for the fictional hair salon Carly’s Clippers. My job? Use three basic lists to calculate average prices, revenue, and potential marketing insights.

### Project Overview

The project gave me three parallel lists:
- `hairstyles`: the haircut names  
- `prices`: the price of each haircut  
- `last_week`: how many times each haircut was sold last week  

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ibvqaegmfiy7wxhntdj7.png)

Each index in the lists matched up across the three—so I could track price, name, and sales quantity together. The tasks were clear:
- Find the average haircut price  
- Adjust the inflated pricing
- Calculate total revenue and average daily revenue  
- Highlight haircuts that will be under $30 next week  

### Starting Points

- Loop through a list and add each item to get a total  
- Use `len()` to calculate averages  
- Apply list comprehensions to modify and filter data  
- Use `range(len(list))` to iterate by index  

---

## Enhancing the Experience

### Discovering `sum()`

One of my favorite moments during this project came when I caught myself thinking, *There has to be a simpler way to sum these prices. * I was looping manually through the list like this:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mry3z8qxe8kdoj8pw3ny.png)

…and then I found the beautiful little shortcut sum()! `total_price = sum(prices)`. It felt like leveling up and not just solving the problem.

### Cutting Prices with Comprehension

Carly wanted to reduce prices across the board by $5. That was my cue to use list comprehension:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bt39v6vk719aa20nlu1h.png)

Here’s where things got tricky. Even though list comprehension looks concise, I still find myself having to slow down and mentally unpack what’s going on. I know it’ll get easier with practice, but for now, I still need to break the logic down piece by piece.

### Tracking Revenue

To calculate revenue, I needed to multiply each haircut price by the number of times it was sold—then add all those up. Here’s where I leaned into the range() function:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ai3tm6d5bnxgl3irona1.png)

This was a satisfying little loop that showed me the power of working with index values when your lists are aligned.

### Filtering by Price

Finally, I used a list comprehension again to find all haircuts that would be under $30 after the price cut:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vis4fizhtrwk69ctgur3.png)

This one was a bit of a brain-bender. I really had to slow down and ask myself: *What am I pulling? From where? And under what condition?* It took a few tries to get right—and I’m okay with that. These are exactly the reps I need.

---

## Lessons Learned

- `sum()` is a fantastic built-in shortcut for adding lists—and worth using whenever possible  
- List comprehensions are powerful, but still feel abstract to me. I'm learning to slow down and break them apart  
- Parallel lists are easier to work with using index-based loops (`range(len(...))`)  
- Even “simple” logic can reveal gaps in understanding—and that’s where the best growth happens  

---

## Final Thoughts

This project was short, clear, and incredibly valuable. The logic wasn’t complex, but it forced me to apply multiple list operations together—and more importantly, to slow down and *understand* what each piece of code was actually doing.

I still find myself second-guessing list comprehensions and occasionally getting stuck in the weeds with loops. But every time I solve one of these problems, it sticks a little more.

Next, I’d love to take this project and modularize it—maybe write a function to print a report summary or allow Carly to update styles dynamically. That’s a challenge for another day, though.

For now, I’m celebrating a working script, a few “aha!” moments, and another piece of my beginner puzzle falling into place.

If you’re also learning Python or exploring Codecademy’s path, I’d love to hear how you’d approach a project like this. Let’s keep growing—one cut, one loop, one list at a time.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yeaqb4yklrn9qkgufpm4.png)
