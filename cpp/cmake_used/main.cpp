#include <iostream>

int main(int, char**) {

    class Date{
        private:
        int year;
        int month;
        int day;

        public:
        void setdate(int year,int month,int day){
            this->year = year;
            this->month = month;
            this->day = day;
        }

        void showdate(){
            std::cout << year << "년" << month << "월" << day << "일"<< std::endl;
        }
    };

    Date a;

    a.setdate(22,2,24);
    a.showdate();

    return 0;
}