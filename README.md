![MyndMap Logo](Website/Front%20Page%202.png)

# MyndMap

MyndMap is a web application designed to help individuals with ADHD improve their focus and productivity. It leverages AI technology to adapt to each user's unique needs and provide personalized assistance. This README provides an overview of the project, its features, installation instructions, and how to contribute.

## Features

- **Personalized AI Assistance**: MyndMap uses advanced AI algorithms to adapt to each user's specific needs, providing tailored strategies and recommendations for improving focus and productivity.

- **ADHD Assessment**: The application includes a comprehensive ADHD assessment based on the DSM-5 criteria. Users can complete the assessment to gauge the severity of their struggles and receive personalised recommendations.

- **Task Organization and Reminders**: MyndMap helps users organize their tasks and provides reminders to stay on track. It allows users to set priorities, deadlines, and track their progress.

- **Subscription Plans**: MyndMap offers different subscription plans, including a basic plan, a Pro plan, and an Elite plan. The Pro and Elite plans provide access to advanced features and enhanced AI assistance.

- **User Profiles**: Users can create profiles to customize their MyndMap experience. They can track their progress, view analytics, and access personalized recommendations.

## Installation

To install and run MyndMap locally, follow these steps:

1. Clone the repository:

git clone https://github.com/your-username/myndmap.git


2. Navigate to the project directory:

cd myndmap


3. Install the required dependencies:

pip install -r requirements.txt


4. Set up the database:

- Create a MySQL database and update the database credentials in the `config.py` file.

- Run the database migration commands:

  ```
  flask db init
  flask db migrate
  flask db upgrade
  ```

5. Start the Flask development server:

flask run


6. Access MyndMap in your web browser:

http://localhost:5000


## Contributing

We welcome contributions to MyndMap! To contribute to the project, follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch for your feature or bug fix:

git checkout -b feature/my-feature


3. Make your changes and commit them with descriptive messages.

4. Push your changes to your forked repository:

git push origin feature/my-feature


5. Open a pull request on the main repository.

Please ensure that your contributions adhere to the project's coding guidelines and standards.

## Roadmap

The following features and enhancements are planned for future releases of MyndMap:

- Integration with calendar and task management applications

- Gamification elements to increase user engagement

## License

MyndMap is open-source software released under the [MIT License](LICENSE).



