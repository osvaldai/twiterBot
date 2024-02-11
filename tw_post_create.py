import os
from datetime import datetime, timedelta

# Calculate the name of the month two months ahead
two_months_ahead_date = datetime.now() + timedelta(days=90)  # Roughly 2 months into the future
two_months_ahead = two_months_ahead_date.strftime('%B')

# Create the month folder
if not os.path.exists(two_months_ahead):
    os.mkdir(two_months_ahead)

# New posts for each week of the subsequent month
two_months_posts = {
    'Week 1': [
        "Meet Olena, who found safety with us after losing her home. Her strength inspires us every day. #BraveChildren #UkraineStrong",
        "A moment of joy amidst chaos: The Ivanov family reunites after weeks of separation. #FamilyReunion #HopeEndures",
        "Education can't wait. We're setting up temporary classrooms for children displaced by conflict. #EducationMatters #LearningUnderFire",
        "Volunteer hero: Anna's tireless efforts bring food and comfort to those in need. #VolunteerPower #HumanitarianHeroes",
        "In war, mental scars are as deep as physical ones. We're providing counseling for our young heroes. #MentalHealth #HealingJourney",
        "Together, we're stronger. A big thank you to our local community for their unwavering support. #CommunityLove #TogetherForUkraine",
        "This week's stories have touched our hearts. Your support makes them possible. #WeeklyReflection #Gratitude"
    ],
    'Week 2': [
        "Safe shelter is a basic need. We're working to provide temporary housing for displaced families. #ShelterForAll #SafeHaven",
        "Urgent call: We need medical supplies to aid injured children. Every contribution counts. #MedicalSupport #UrgentAid",
        "Protecting unaccompanied children is a priority. Help us keep them safe. #ProtectOurChildren #LostTooYoung",
        "Play is healing. We're distributing toys and games to bring smiles to children's faces. #PlayHeals #JoyInCrisis",
        "Nutritious meals are essential for growth and health. We're ensuring no child goes to bed hungry. #FeedTheFuture #NutritionMatters",
        "We're providing books and educational materials to keep the flame of learning burning. #EducationForPeace #LearningLights",
        "This week, we've tackled crucial needs head-on. Thanks to your support, we're making a difference. #WeeklyImpact #TogetherStrong"
    ],
    'Week 3': [
        "Join our mission. Your donation can change lives. Every bit helps. #DonateNow #EveryContributionCounts",
        "From our volunteer diary: Maria shares her experiences and the smiles she's seen. #VolunteerDiaries #HeartwarmingTales",
        "Access to clean water is a right. We're on the ground, ensuring clean water for children and families. #CleanWaterForAll #LifeSource",
        "Education can change the world, even in the darkest times. Support our educational programs. #EducationIsPower #FutureBuilders",
        "Your donations at work: See how your contributions have transformed lives. #DonationsAtWork #ImpactfulChange",
        "Every small victory counts. Today, a group of children returned to school, thanks to your support. #SmallVictories #BackToSchool",
        "Your engagement this week has been incredible. Together, we're building a better tomorrow. #WeeklyEngagement #Thankful"
    ],
    'Week 4': [
        "We dream of a peaceful, safe future for every Ukrainian child. Join us in making this dream a reality. #DreamsOfPeace #FutureForChildren",
        "It takes a village. Grateful for the global community's support in these trying times. #GlobalSupport #UnityInCrisis",
        "Rebuilding lives, one day at a time. Join our efforts to restore homes and hope. #RebuildingLives #HopeRestored",
        "Urgent need for warm clothing as temperatures drop. Help us provide comfort. #WarmthForKids #UrgentNeeds",
        "The road to recovery is long. Commit to long-term support and make a lasting difference. #LongTermSupport #CommitToChange",
        "Children's resilience in the face of adversity is our inspiration. Let's support their strength. #Resilience #Inspiration",
        "As May ends, we reflect on the incredible journey and the strides made. Here's to continued efforts and hope. #MonthInReview #HopeContinues"
    ]
}

# Iterate through the weeks and create folders and files
for week, week_posts in two_months_posts.items():
    week_folder = os.path.join(two_months_ahead, week)

    # Create week folder
    if not os.path.exists(week_folder):
        os.mkdir(week_folder)

    # Create files for each post
    for idx, post in enumerate(week_posts, start=1):
        file_name = os.path.join(week_folder, f"Day {idx}.txt")

        with open(file_name, 'w') as file:
            file.write(post)

print(f"Created posts for {two_months_ahead}!")
# import os
# from datetime import datetime
#
#
# def get_today_post():
#     # Get the current month name and day of the week
#     current_month = datetime.now().strftime('%B')
#     current_week_of_month = (datetime.now().day - 1) // 7 + 1  # Convert day to week of month (1-4)
#     current_day_of_week = datetime.now().weekday() + 1  # .strftime('Day %A')  # Convert to format like "Day Monday"
#     week_folder_name = f"Week {current_week_of_month}"
#     file_name = f"Day {current_day_of_week}.txt"
#
#     # Path to the file
#     file_path = os.path.join("/Users/vladislavpidberezhnik/Desktop/Новая_папка/twitter_post", current_month,
#                              week_folder_name, file_name)
#     print(file_path)
#     # Check if the file exists
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as file:
#             post_content = file.read()
#             return post_content
#     else:
#         return "No post found for today!"
#
#
# print(get_today_post())
