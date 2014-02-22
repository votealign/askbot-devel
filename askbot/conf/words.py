"""
General skin settings
"""
from askbot.conf.settings_wrapper import settings
from askbot.deps.livesettings import ConfigurationGroup
from askbot.deps.livesettings import values
from django.utils.translation import ugettext_lazy as _
from askbot.skins import utils as skin_utils
from askbot import const
from askbot.conf.super_groups import CONTENT_AND_UI

WORDS = ConfigurationGroup(
                    'WORDS',
                    _('Site terms vocabulary'),
                    super_group = CONTENT_AND_UI
                )

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_YOUR_QUESTION',
        default=_('Post New Decision'),
        description=_('Post New Decision'),
        help_text=_('Used on a button')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_ENTER_YOUR_QUESTION',
        default=_('Describe new decision'),
        description=_('Describe new decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_THE_GROUP',
        default=_('Ask the Group'),
        description=_('Ask the Group'),
        help_text=_('Used on a button')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_POST_YOUR_ANSWER',
        default=_('Post Your Summary'),
        description=_('Post Your Summary'),
        help_text=_('Used on a button')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_YOUR_OWN_QUESTION',
        default=_('Summarize Your Own Decision'),
        description=_('Summarize Your Own Decision'),
        help_text=_('Used on a button')
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_TO_ANSWER_OWN_QUESTION',
        default=_(
            '<span class="big strong">You are welcome to summarize your own decision</span>, '
            'but please make sure to give an <strong>summary</strong>. '
            'Remember that you can always <strong>revise your original decision</strong>.'
        ),
        description=_('Instruction to summarize own post'),
        help_text=_('HTML is allowed')
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_TO_POST_ANONYMOUSLY',
        default=_(
            '<span class="strong big">Please start posting anonymously</span> - '
            'your entry will be published after you log in or create a new account.'
        ),
        description=_('Instruction to post anonymously'),
        help_text=_('HTML is allowed')
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_TO_GIVE_ANSWERS',
        default=_(
            'Please try to <strong>give a substantial summary</strong>, '
            'for discussions, <strong>please use comments</strong> and '
            '<strong>do remember to vote</strong>.'
        ),
        description=_('Instruction to give summaries'),
        help_text=_('HTML is allowed')
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_FOR_THE_CATEGORY_SELECTOR',
        default=_(
            'Categorize your decision using this tag selector or '
            'entering text in tag box.'
        ),
        description=_('Instruction for the catogory selector'),
        help_text=_('Plain text only')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_EDIT_YOUR_PREVIOUS_ANSWER',
        default=_('Edit Your Previous Answer'),
        description=_('Edit Your Previous Answer'),
        help_text=_('Used on a button')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_QUESTIONS',
        default=_('post decisions'),
        description=_('post decisions')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED',
        default=_('asked'),
        description=_('asked'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED_FIRST_QUESTION',
        default=_('Posted first Decision'),
        description=_('Posted first Decision')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED_BY_ME',
        default=_('Asked by me'),
        description=_('Asked by me')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED_A_QUESTION',
        default=_('Asked a decision'),
        description=_('Asked a decision')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED_A_QUESTION',
        default=_('Summarized a decision'),
        description=_('Summarized a decision')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED_BY_ME',
        default=_('Summarized by me'),
        description=_('Summarized by me')
    )
)


settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPTED_AN_ANSWER',
        default=_('accepted a summary'),
        description=_('accepted a summary')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GAVE_ACCEPTED_ANSWER',
        default=_('Gave accepted summary'),
        description=_('Gave accepted summary')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED',
        default=_('summarized'),
        description=_('summarized'),
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_QUESTIONS_COUNTABLE_FORMS',
        default='decision\decisions',
        description=_('Countable plural forms for "decision"'),
        help_text=_('Enter one form per line, pay attention')
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_ANSWERS_COUNTABLE_FORMS',
        default='summary\summaries',
        description=_('Countable plural forms for "summary"'),
        help_text=_('Enter one form per line, pay attention')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_SINGULAR',
        default=_('decision'),
        description=_('decision (noun, singular)'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_PLURAL',
        default=_('decisions'),
        description=_('decisions (noun, plural)'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UNANSWERED_QUESTION_SINGULAR',
        default=_('unsummarized decision'),
        description=_('unsummarized decisions (singular)'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UNANSWERED_QUESTION_PLURAL',
        default=_('unsummarized decisions'),
        description=_('unsummarized decisions (plural)'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_SINGULAR',
        default=_('summary'),
        description=_('summary (noun, sungular)'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_VOTED_UP',
        default=_('Decision voted up'),
        description=_('Decision voted up'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_VOTED_UP',
        default=_('Summary voted up'),
        description=_('Summary voted up'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UPVOTED_ANSWER',
        default=_('upvoted summary'),
        description=_('upvoted summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NICE_ANSWER',
        default=_('Nice Summary'),
        description=_('Nice Summary'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NICE_QUESTION',
        default=_('Nice Decision'),
        description=_('Nice Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GOOD_ANSWER',
        default=_('Good Summary'),
        description=_('Good Summary'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GOOD_QUESTION',
        default=_('Good Decision'),
        description=_('Good Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GREAT_ANSWER',
        default=_('Great Summary'),
        description=_('Great Summary'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GREAT_QUESTION',
        default=_('Great Decision'),
        description=_('Great Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_POPULAR_QUESTION',
        default=_('Popular Decision'),
        description=_('Popular Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NOTABLE_QUESTION',
        default=_('Notable Decision'),
        description=_('Notable Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FAMOUS_QUESTION',
        default=_('Famous Decision'),
        description=_('Famous Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_STELLAR_QUESTION',
        default=_('Stellar Decision'),
        description=_('Stellar Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FAVORITE_QUESTION',
        default=_('Favorite Decision'),
        description=_('Favorite Decision'),
        help_text='Badge name'
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UPVOTED_ANSWERS',
        default=_('upvoted summaries'),
        description=_('upvoted summaries'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_SHOW_ONLY_QUESTIONS_FROM',
        default=_('Show only decisions from'),
        description=_('Show only decisions from'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_ASK_YOUR_QUESTION_HERE',
        default=_('Post new decision here'),
        description=_('Post new decision here'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_THIS_QUESTION_HAS_BEEN_DELETED',
        default=_(
                'Sorry, this decision has been '
                'deleted and is no longer accessible'
            ),
        description=_('This decision has been deleted')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_ENTER_YOUR_QUESTION',
        default=_('Describe new decision'),
        description=_('Describe new decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_DELETE_YOUR_QUESTION',
        default=_('remove this decision'),
        description=_('remove this decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_A_QUESTION_INTERESTING_TO_THIS_COMMUNITY',
        default=_('post a decision that is interesting to this community'),
        description=_('post a decision that is interesting to this community'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NO_QUESTIONS_HERE',
        default=_('No decision here.'),
        description=_('No decision here.'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_FOLLOW_QUESTIONS',
        default=_('Please follow some decisions or follow some users.'),
        description=_('Please follow some decisions or follow some users.'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_FEEL_FREE_TO_ASK_YOUR_QUESTION',
        default=_('Please feel free to add a new decision!'),
        description=_('Please feel free to add a new decision!'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_SWAP_WITH_QUESTION',
        default=_('swap with decision'),
        description=_('swap with decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_REPOST_AS_A_QUESTION_COMMENT',
        default=_('repost as a decision comment'),
        description=_('repost as a decision comment'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ONLY_ONE_ANSWER_PER_USER_IS_ALLOWED',
        default=_('(only one summary per user is allowed)'),
        description=_('Only one summary per user is allowed'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPT_BEST_ANSWERS_FOR_YOUR_QUESTIONS',
        default=_('Accept the best summary of decisions'),
        description=_('Accept the best summary of decisions')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_AUTHOR_OF_THE_QUESTION',
        default=_('author of the decision'),
        description=_('author of the decision')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPT_OR_UNACCEPT_THE_BEST_ANSWER',
        default=_('accept or unaccept the best summary'),
        description=_('accept or unaccept the best summary')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPT_OR_UNACCEPT_OWN_ANSWER',
        default=_('accept or unaccept your own summary'),
        description=_('accept or unaccept your own summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_YOU_ALREADY_GAVE_AN_ANSWER',
        default=_('you already gave a summary'),
        description=_('you already gave a summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GAVE_AN_ANSWER',
        default=_('gave a summary'),
        description=_('gave a summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_OWN_QUESTIONS',
        default=_('summarize own post'),
        description=_('summarize own post'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED_OWN_QUESTION',
        default=_('Summarized own post'),
        description=_('Summarized own post'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_REPOST_AS_A_COMMENT_UNDER_THE_OLDER_ANSWER',
        default=_('repost as a comment under older summary'),
        description=_('repost as a comment under older summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_INVITE_OTHERS_TO_HELP_ANSWER_THIS_QUESTION',
        default=_('invite other to help summarize this decision'),
        description=_('invite other to help summarize this decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_RELATED_QUESTIONS',
        default=_('Related decisions'),
        description=_('Related decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_TOOLS',
        default=_('Summary Tools'),
        description=_('Summary Tools'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_THIS_QUESTION_IS_CURRENTLY_SHARED_ONLY_WITH',
        default=_('Phrase: this decision is currently shared only with:'),
        description=_('Phrase: this decision is currently shared only with:'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_BE_THE_FIRST_TO_ANSWER_THIS_QUESTION',
        default=_('Be the first one to summarize this decision!'),
        description=_('Be the first one to summarize this decision!'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FOLLOWED_QUESTIONS',
        default=_('followed decisions'),
        description=_('followed decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FOLLOW_QUESTIONS',
        default=_('follow decisions'),
        description=_('follow decisions'),
        help_text=_('Indefinite form')
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_COMMENTS_AND_ANSWERS_TO_OTHERS_QUESTIONS',
        default = '',
        description = _('Phrase: comments on and summaries of decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_YOU_CAN_POST_QUESTIONS_BY_EMAILING_THEM_AT',
        default=_('You can post decisions by emailing them at'),
        description=_('You can post decisions by emailing them at'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_LIST_OF_QUESTIONS',
        default=_('List of decisions'),
        description=_('List of decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_COMMUNITY_GIVES_YOU_AWARDS',
        default=_('Community gives you awards for your posts, summaries and votes'),
        description=_('Community gives you awards for your posts, summaries and votes'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_CLOSE_QUESTION',
        default=_('Close decisions'),
        description=_('Close decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_CLOSE_QUESTIONS',
        default=_('close decisions'),
        description=_('close decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_EDIT_QUESTION',
        default=_('Edit decision'),
        description=_('Edit decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_IN_ONE_SENTENCE',
        default=_('Decision - in one sentence'),
        description=_('Decision - in one sentence'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_RETAG_QUESTION',
        default=_('Retag decision'),
        description=_('Retag decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_RETAG_QUESTIONS',
        default=_('retag decisions'),
        description=_('retag decisions'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_REOPEN_QUESTION',
        default=_('Reopen decision'),
        description=_('Reopen decision'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_THERE_ARE_NO_UNANSWERED_QUESTIONS_HERE',
        default=_('There are no unsummarized decisions here'),
        description=_('There are no unsummarized decisions here'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_THIS_ANSWER_HAS_BEEN_SELECTED_AS_CORRECT',
        default=_('this summary has been selected as most accurate'),
        description=_('this summary has been selected as most accurate'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_MARK_THIS_ANSWER_AS_CORRECT',
        default=_('mark this sumamry as accurate'),
        description=_('mark this sumamry as accurate'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_LOGIN_SIGNUP_TO_ANSWER',
        default=_('Login/Signup to Summarize'),
        description=_('Login/Signup to Summarize'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_YOUR_ANSWER',
        default=_('Your Summary'),
        description=_('Your Summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ADD_ANSWER',
        default=_('Add Summary'),
        description=_('Add Summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GIVE_AN_ANSWER_INTERESTING_TO_THIS_COMMUNITY',
        default=_('give a summary interesting to this community'),
        description=_('give a summary interesting to this community'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GIVE_AN_ANSWER_INTERESTING_TO_THIS_COMMUNITY',
        default=_('give a summary interesting to this community'),
        description=_('give a summary interesting to this community'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GIVE_A_GOOD_ANSWER',
        default=_('give a substantial summary'),
        description=_('give a substantial summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_TRY_TO_GIVE_AN_ANSWER',
        default=_('try to give a summary, rather than engage into a discussion'),
        description=_('try to give a summary, rather than engage into a discussion'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_SHOW_ONLY_SELECTED_ANSWERS_TO_ENQUIRERS',
        default=_('show only selected summaries to enquirers'),
        description=_('show only selected summaries to enquirers'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UNANSWERED',
        default = _('NEEDS SUMMARY'),
        description = _('NEEDS SUMMARY'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_EDIT_ANSWER',
        default=_('Edit Summary'),
        description=_('Edit Summary'),
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED',
        default=_('Summarized'),
        description=_('Summarized'),
    )
)
