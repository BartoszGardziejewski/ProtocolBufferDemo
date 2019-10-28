package pwr.protocolbuffer;

import pwr.protocolbuffer.models.PeopleMessage;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Application {

    public static void main(String... args) {
        new Application();
    }

    Application() {
        final String filePath = "../protobufBinary/People";

        PeopleMessage.People people = generateData();

        try {
            serializeData(people, filePath);
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(people);

        try {
            PeopleMessage.People deselizedPeople = deserializeData(filePath);
            System.out.println(deselizedPeople);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private PeopleMessage.People generateData() {
        PeopleMessage.Person personBG =
                PeopleMessage.Person.newBuilder()
                        .setFName("Bill")
                        .setLName("Gates")
                        .setAge(64)
                        .setIsFamous(true)
                        .build();

        PeopleMessage.Person personSJ =
                PeopleMessage.Person.newBuilder()
                        .setFName("Steve")
                        .setLName("Jobs")
                        .setAge(64)
                        .build();

        PeopleMessage.Person personAT =
                PeopleMessage.Person.newBuilder()
                        .setFName("Alan")
                        .setLName("Turing")
                        .build();

        PeopleMessage.People people =
                PeopleMessage.People.newBuilder()
                        .addPerson(personBG)
                        .addPerson(personSJ)
                        .addPerson(personAT)
                        .build();

        return people;
    }

    private void serializeData(PeopleMessage.People people, String filePath) throws IOException {
        FileOutputStream fos = new FileOutputStream(filePath);
        people.writeTo(fos);
    }

    private PeopleMessage.People deserializeData( String filePath) throws IOException {
        return PeopleMessage.People.newBuilder().mergeFrom(new FileInputStream(filePath)).build();
    }
}
