ratings = {RatingScore: "{{average_rate}}" } 
totalRating = 5;
table = document.querySelector('.RatingStar');
  
  function rateIt() {
    for (rating in ratings) {
    ratingPercentage = ratings[rating] / totalRating * 100;
    ratingRounded = Math.round(ratingPercentage / 10) * 10 + '%';
    star = table.querySelector(`.${rating} .inner-star`);
    numberRating = table.querySelector(`.${rating} .numberRating`);
    star.style.width = ratingRounded;
    numberRating.innerText = ratings[rating]
    }
  }
