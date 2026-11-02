// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentRecords {
    struct Student {
        uint256 rollNo;
        string name;
        uint256 marks;
    }

    Student[] public students;
    uint256 public fallbackCalls;

    // Add a student
    function addStudent(
        uint256 _rollNo,
        string memory _name,
        uint256 _marks
    ) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Get student details using array index
    function getStudent(uint256 _index)
        public
        view
        returns (uint256, string memory, uint256)
    {
        require(_index < students.length, "Invalid student index");

        Student memory s = students[_index];
        return (s.rollNo, s.name, s.marks);
    }

    // Get total number of students
    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    // Handles calls that do not match any function
    fallback() external payable {
        fallbackCalls++;
    }
    receive() external payable {
    // Accept ETH sent directly to the contract
}
}
