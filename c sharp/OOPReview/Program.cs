using System;

namespace OOPReview
{
     /// <summary>
     /// This is an interface. The sole purpose of an interface is to define the
     /// shape of something (or the ABSTRACTION). This is not an example of
     /// inheritance. Because all Echoers implement (conform to) this interface,
     /// we can declare one variable of type IEchoer in Main and simply reassign
     /// different Echoers to it.
     /// </summary>
    public interface IEchoer
    {
        void Echo(string message);
    }

    /// <summary>
    /// This is the simplest case of implementing an interface. Because the
    /// IEchoer interface declares a single method (Echo) we need to implement
    /// that method here or the code won't even compile.
    ///
    /// Also note that Echo here is 'virtual'. In C#, this means that
    /// subclasses can choose whether to override it with a different
    /// implementation. 
    /// </summary>
    public class Echoer : IEchoer
    {
        public virtual void Echo(string message)
        {
            Console.WriteLine(message);
        }
    }

    /// <summary>
    /// This is a simple example of inheritance. Here we are inheriting from
    /// Echoer, which implements IEchoer. So, we are also implicitly implementing
    /// (conforming to) IEchoer.
    ///
    /// Also, notice that, while Echoer has its own implementation of Echo,
    /// we're choosing a different implementation here by overriding Echoer's
    /// virtual Echo.
    /// </summary>
    public class WrappedEchoer : Echoer
    {
        public override void Echo(string message)
        {
            Console.WriteLine("HEADER");
            base.Echo("    " + message);
            Console.WriteLine("FOOTER");
        }
    }

    /// <summary>
    /// This is simply a class with a constructor. It's primarily here so
    /// we can see how private members and base constructors work with
    /// inheritance.
    /// </summary>
    public class PersonalizedEcoher : IEchoer
    {
        private string _name;
        
        public PersonalizedEcoher(string yourName)
        {
            _name = yourName;
        }

        public virtual void Echo(string message)
        {
            Console.WriteLine(_name + " asked me to echo: " + message);
        }
    }

    /// <summary>
    /// Here we are creating a new class which demonstrates calling a
    /// base constructor as well as how 'private' can hide members,
    /// even from subclasses.
    ///
    /// You must call the base constructor using :base(name). Try
    /// commenting that out here and see what error you get on
    /// compilation. 
    /// </summary>
    public class AngryPersonalizedEchoer : PersonalizedEcoher
    {
        public AngryPersonalizedEchoer(string name) : base(name)
        {
            //note that I can't directly access _name here, because it is private.
            //what happens if I go to PersonalizedEchoer and change it to protected?
        }

        public override void Echo(string message)
        {
            base.Echo(message.ToUpper());
        }
    }
    
    /// <summary>
    /// We still needed to cover 'abstract' and 'protected'. We'll use EchoerBase,
    /// AngryEchoer, and WhisperEchoer to cover this.
    ///
    /// First, EchoerBase is an abstract class. This means you can't directly
    /// instantiate it. To understand what I mean, go to the Main and try the
    /// following line. It won't compile:
    /// var e = new EchoerBase();
    /// </summary>
    public abstract class EchoerBase : IEchoer
    {
        protected string _originalMessage;
        
        public abstract void Echo(string message);

        protected string MakeAngry(string message)
        {
            return message.ToUpper();
        }

        protected string MakeWhisper(string message)
        {
            return message.ToLower();
        }

        /// <summary>
        /// This is a C# property. It's some syntactic sugar around
        /// the old notion of getters and setters. There are more
        /// modern features that make this easier to read, but I'm
        /// trying to limit how much C# you have to learn.
        /// </summary>
        public string OriginalMessage
        {
            get { return _originalMessage; }
        }
    }
    
    /// <summary>
    /// To create a subclass, we are required to provide an override implementation
    /// for Echo (because it is an abstract method). Also, note that we have access
    /// to protected methods from the base class. 
    /// </summary>
    public class AngryEchoer : EchoerBase
    {
        public override void Echo(string message)
        {
            _originalMessage = message;
            Console.WriteLine(MakeAngry(message));
        }
    }

    /// <summary>
    /// To create a subclass, we are required to provide an override implementation
    /// for Echo (because it is an abstract method). Also, note that we have access
    /// to protected methods from the base class. 
    /// </summary>
    public class WhisperEchoer : EchoerBase
    {
        public override void Echo(string message)
        {
            _originalMessage = message;
            Console.WriteLine(MakeWhisper(message));
        }
    }

    /// <summary>
    /// This is not object-oriented programming, but a common antipattern. When you
    /// have static classes (or even static methods on a non-static class) you're
    /// no longer working with an instance. Instead, in this example, we only ever
    /// have one StaticEchoer. We could remove the 'static' from the class declaration
    /// and leave it on the method. Then we'd be able to instantiate the class to
    /// create an object. However, if we leave 'static' on the method, we'd still
    /// only be able to call it on the class.
    ///
    /// We will make very limited use of static classes or methods this semester.
    /// </summary>
    public static class StaticEchoer
    {
        public static void Echo(string message)
        {
            Console.WriteLine(message);
        }
    }
    
    public class Program 
    {
        public static void Main(string[] args) 
        {
            //I recommend a couple of exercises here.
            //1. Try declaring echoer as Echoer instead of IEchoer. What fails?
            //2. Try using the keyword 'var' instead of IEchoer. Then what type is echoer?
            IEchoer echoer = new Echoer();
            echoer.Echo("Hello World!");
            //((Echoer)echoer).HelloWorld(); 
            // --> CASTING. its literally telling the program not to worry about things, it is what it is
            // --> this is implementing an interface, NOT INHERITING from an interface.
            // we IMPLENT AN INTERFACE. we INHERIT A CLASS
            // --> you can cast to an interface

            echoer = new AngryEchoer();
            echoer.Echo("Hello World!");
            Console.WriteLine("The original message was " + ((AngryEchoer)echoer).OriginalMessage);
            //That previous line performs a cast. Why do we need a cast here? Remove it to find out.  
            
            echoer = new WhisperEchoer();
            echoer.Echo("Hello World!");
            Console.WriteLine("The original message was " + ((WhisperEchoer)echoer).OriginalMessage);
            //That previous line performs a cast. Why do we need a cast here? Remove it to find out.  
            
            echoer = new WrappedEchoer();
            echoer.Echo("Hello World!");

            echoer = new PersonalizedEcoher("Lucas");
            echoer.Echo("Hello World!");
            
            echoer = new AngryPersonalizedEchoer("Lucas");
            echoer.Echo("Hello World!");

            //This won't work because EchoerBase is abstract.
            //var e = new EchoerBase();

            StaticEchoer.Echo("Static Hello World!");
            
        }
    }
}