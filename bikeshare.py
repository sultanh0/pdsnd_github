import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def invalid_input():
        print ("\nYour input is invalid.\nWould you like to restart? Enter yes or no")
        restart = input(  )
        if restart.lower() == 'yes':
                print('-'*40)
                main()
        if restart.lower() != 'no':
            invalid_input()
        else:
            return
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ( 'Choice one of these Cities : Chicago, New York, or Washington:  ').lower()
        if city in  ['chicago' , 'new york' , 'washington']:
            break 
        else:
            invalid_input()
            
    # TO DO: get user input for month (January, February, March, April, May, June, July, August, September, October, November, December.)
    while True:
        month = input ( 'Choice one month OR all  [ January, February, March, April, May, June. ]:  ').lower()
        if month in  [ "january", "february", "march", "april", "may", "june", "all" ]:
            break
        else:
            invalid_input()        

    # TO DO: get user input for day of week (  Monday,Tuesday, Wednesday, Thursday, Friday, Saturday. Sunday )
    while True:
        day = input ( 'Choice one weekday OR all [  Monday,Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ]:  ').lower()
        if day in  ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"] :
            break 
        else:
            invalid_input()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
   # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
   # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # extract  day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
      # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':   
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n*** Calculating The Most Frequent Times of Travel... ***\n')
    start_time = time.time()

    # TO DO: display the most common month
    [month]=df['month'].mode()
    print('Most Common month: ',month)

    # TO DO: display the most common day of week
    [day]=df['day_of_week'].mode()
    print('Most Common day: ', day)

    # TO DO: display the most common start hour
    [hour]=df['hour'].mode()
    print('Most Common hour:  ',hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n*** Calculating The Most Popular Stations and Trip... ***\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Common start station: ',start_station)
    
    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most Common end station: ',end_station)

    # display most frequent combination of start station and end station trip
    combine_stations = df['Start Station'] + "  *  " + df['End Station']
    combination_station = combine_stations.value_counts().idxmax()
    print ('Most frequent combination stations: \nstart FROM {} \nend TO {}'.format(combination_station.split("  *  ")[0], combination_station.split("  *  ")[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n*** Calculating Trip Duration... ***\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_Trip_Duration = df['Trip Duration'].sum()
    print('Total trip durationr= ',total_Trip_Duration )

    # TO DO: display mean travel time
    avg_Trip_Duration = df['Trip Duration'].mean()
    print('Avrege trip durationr= ',avg_Trip_Duration )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\n*** Calculating User Stats... ***\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Types of accounts users :\n{} '.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nThe gender of the account user: \n{}'.format(gender))
        
   # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\nThe age account users:" )
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print("Earliest year of birth: " + str(earliest))
        print("Most recent year of birth: " + str(recent))
        print("Most common year of birth: " + str(common))
           
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
def raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while True:
        try:
            if user_input.lower() != 'no':
                if user_input.lower() == 'yes':
                   print(df.iloc[line_number : line_number+5])
                   line_number +=5
                   user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        except KeyboardInterrupt:
                 return
            
def main():
     while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

if __name__ == "__main__":
	main()