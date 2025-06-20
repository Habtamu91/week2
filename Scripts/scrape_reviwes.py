import pandas as pd
from google_play_scraper import Sort, reviews


def scrape_reviews(app_id, bank_name, lang='en', country='et', total_reviews=1200):
    all_reviews = []
    count = 0

    while len(all_reviews) < total_reviews:
        new_reviews, _ = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.NEWEST,
            count=400,
            filter_score_with=None
        )
        if not new_reviews:
            print(f"No more reviews returned for {bank_name}.")
            break

        all_reviews.extend(new_reviews)
        count += 1
        if count > 5:
            print(f"Limit reached for {bank_name}.")
            break

    cleaned_data = []
    for review in all_reviews:
        cleaned_data.append({
            'review': review.get('content', ''),
            'rating': review.get('score', None),
            'date': review.get('at', None),
            'bank': bank_name,
            'source': 'Google Play'
        })

    return pd.DataFrame(cleaned_data)
bank_apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}
all_banks = pd.DataFrame()
for bank, app_id in bank_apps.items():
    print(f"Scraping reviews for {bank}...")
    df = scrape_reviews(app_id, bank)
    all_banks = pd.concat([all_banks, df], ignore_index=True)
    all_banks['date'] = pd.to_datetime(all_banks['date']).dt.date
 





# Save the cleaned combined reviews once
if bank:
   all_banks.to_csv('raw_reviews.csv', index=False)
   print("✅ Reviews saved to raw_reviews.csv")
else:
    print("❌ No reviews were scraped.")